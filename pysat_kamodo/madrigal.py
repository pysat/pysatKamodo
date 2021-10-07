from pysat_kamodo import Pysat_Kamodo


import pysatMadrigal

import pysat
pysat.utils.registry.register(['pysatMadrigal.instruments.dmsp_ivm',
                               'pysatMadrigal.instruments.jro_isr'])


class Madrigal_Kamodo(Pysat_Kamodo):
    def __init__(self,
                 date,
                 user, # required for madrigal database access
                 password, # required for madrigal database access
                 verbose=False,
                 **kamodo_kwargs):
        self._user = user
        self._password = password
        self.verbose = verbose
        super(Madrigal_Kamodo, self).__init__(date, verbose=verbose, **kamodo_kwargs)
    
    def load_data(self, date):
        """Attempt to load data if available, else download"""
        self._instrument.load(date = date)
        if self._instrument.data.empty:
            self._instrument.download(start = date, stop = date, user=self._user, password=self._password)
            self._instrument.load(date = date)
