```python
from pysat_kamodo.nasa import Pysat_Kamodo
```

```python
kcnofs = Pysat_Kamodo('2009, 1, 1', # Pysat_Kamodo allows string dates
         platform = 'cnofs', # pysat keyword
         name='vefi', # pysat keyword
         tag='dc_b',# pysat keyword
         )
```

```python
kcnofs
```
