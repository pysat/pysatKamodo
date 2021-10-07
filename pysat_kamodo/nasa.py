# ---
# jupyter:
#   jupytext:
#     formats: py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import pysat
import pysatNASA
pysat.utils.registry.register_by_module(pysatNASA.instruments)

# the above line ensures that the NASA instruments are loaded into the pysat namespace
# -

from pysat_kamodo import Pysat_Kamodo 
