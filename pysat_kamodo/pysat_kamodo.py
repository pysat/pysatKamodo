from kamodo.util import get_defaults
from kamodo import kamodofy, Kamodo
import inspect

import pysat

def extract_inst_kwargs(kwargs):
    """extract instrument keywords""" 
    inst_kwarg_names = get_defaults(pysat.Instrument).keys()
    inst_kwargs = {}
    for k in inst_kwarg_names:
        if k in kwargs:
            inst_kwargs[k] = kwargs.pop(k)
    return inst_kwargs

def time_interpolator(timekwarg):
    """{docstring}"""

    # Note: df will be passed into this function's local scope
    # t will be provisioned as a keyword argument

    df_ = df.reindex(df.index.union(t))
    df_interpolated = df_.interpolate(method='time')
    result = df_interpolated.reindex(t)
    return result

time_interpolator_docstring = """{varname} time interpolator

parameters:
t: datetime series or list

returns: {varname} [{units}] pandas series
"""

def get_interpolator(func, varname, df, default_time, docstring):
    """Creates time interpolator with custom signature"""
    #extract source code from time_interpolator
    src = inspect.getsource(time_interpolator)

    #create variable-dependent signature
    new_src = (src \
           .format(docstring = docstring)
           .replace('timekwarg',"t = default_time")
           .replace('time_interpolator', varname))

#     default_time = self._instrument.data.index
    loc = dict(default_time = default_time, df = df)
    exec(new_src, loc)
    return loc[varname]

class Pysat_Kamodo(Kamodo):
    def __init__(self, date, **kamodo_kwargs):
        
        inst_kwargs = extract_inst_kwargs(kamodo_kwargs)
        
        self._instrument = pysat.Instrument(**inst_kwargs)

        self.load_data(date)
        
        super(Pysat_Kamodo, self).__init__()
        
        self.register_variables()
        
        for varname, interpolator in kamodo_kwargs.items():
            self[varname] = interpolator
    
    def load_data(self, date):
        """Attempt to load data if available, else download"""
        self._instrument.load(date = date)
        if self._instrument.data.empty:
            self._instrument.download(start = date, stop = date)
            self._instrument.load(date = date)
        
    def register_variables(self):
        """register variables as kamodo functions"""
        
        for varname in self._instrument.data.columns:
            units = self._instrument.meta[varname].units
            if type(units) is not str:
                units = ''

            docstring = time_interpolator_docstring.format(varname = varname, units = units)
            interpolator = get_interpolator(time_interpolator, 
                                            varname,
                                            self._instrument.data[varname],
                                            self._instrument.data.index,
                                            docstring)

            
            self[varname] = kamodofy(interpolator, 
                                     units = units,
                                     citation = "See {} {} instrument docs".format(
                                        self._instrument.platform, self._instrument.name))

    @property
    def meta(self):
        """metadata of the Pysat_Kamodo interface

        meta is a python-in-heliophysics community standard"""
        return self.detail()

    @property
    def data(self):
        """Get data from underlying instrument object

        data is a python-in-heliophysics community standard"""
        return self._instrument.data
    
    






