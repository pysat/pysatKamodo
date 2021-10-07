from pysat_kamodo import Pysat_Kamodo


import pysatMadrigal

import pysat
pysat.utils.registry.register(['pysatMadrigal.instruments.dmsp_ivm',
                               'pysatMadrigal.instruments.jro_isr'])


# +
class Madrigal_Kamodo(Pysat_Kamodo):
    def __init__(self,
                 date,
                 user, # required for madrigal database access
                 password, # required for madrigal database access
                 default_stride=10,
                 verbose=False,
                 **kamodo_kwargs):
        self._user = user
        self._password = password
        self.verbose = verbose
#         self._skip = 'year', 'month', 'day', 'hour', 'min', 'sec'
        super(Madrigal_Kamodo, self).__init__(date, default_stride=default_stride, verbose=verbose, **kamodo_kwargs)
    
    def load_data(self, date):
        """Attempt to load data if available, else download"""
        self._instrument.load(date = date)
        if self._instrument.data.empty:
            self._instrument.download(start = date, stop = date, user=self._user, password=self._password)
            self._instrument.load(date = date)


dmsp = Madrigal_Kamodo('2001, 1, 1', 'firstname+lastname', 'email@address.com',
                      platform='dmsp', name='ivm', tag='utd',
                      inst_id='f12',
                      regnames = {'+':'plus', '-': 'minus'},
                      default_stride=1,
                      )
# -

dmsp

dmsp.plot('sigma_vy')
