# About

This project tracks development of the kamodo-pysat interface. While pysat focuses
on providing a unified way of retrieving, loading and cleaning instrument data,
Kamodo provides a math-oriented API for interpolation, function composition, 
and quick-look graphics. The combination of the two approaches simplifies 
the workflow for science users, while minimizing the effort needed for science discovery.

## Install

```console
pip install pysat-kamodo
```

## Usage

```python
from pysat_kamodo.pysat_kamodo import Pysat_Kamodo
```

```python
kinst = Pysat_Kamodo('2009, 1, 1', # date required
    platform = 'pysat', # pysat keyword
    name='testing', # pysat keyword
    )
```

```python
# in a jupyter notebook cell, the object renders as a set of 1-d functions
kinst
```

Any of the above functions may be called by passing values for time

```python
import pandas as pd
kinst.dummy1([pd.to_datetime('2009-01-01 15:16:45')])
```

As a subclass of Kamodo, the kinst object automatically plots via function inspection

```python
kinst.plot('dummy1')
```

The code below requires installation of the cnofs instrument.

```python
pki = Pysat_Kamodo('2009, 1, 1', # Pysat_Kamodo allows string dates
                  platform = 'cnofs', # pysat keyword
                  name='vefi', # pysat keyword
                  tag='dc_b',# pysat keyword
                  )

pki.B_up().head()
```
```console
2009-01-01 00:00:00   -3984.774658
2009-01-01 00:00:01   -3966.702637
2009-01-01 00:00:02   -3951.631592
2009-01-01 00:00:03   -3936.454102
2009-01-01 00:00:04   -3921.183594
Name: B_up, dtype: float32
```


## Requirements

`pysat_kamodo` requires `pysat` and `kamodo`:
```console
pip install pysat
pip install kamodo
```

The following are needed for writing publication-ready graphics:

```console
conda install -c plotly plotly-orca
conda install psutil
```

To generate the documentation site:

```console
pip install mkdocs
pip install mknotebooks
pip install python-markdown-math
pip install markdown-include

mkdocs serve (from base directory)
```
