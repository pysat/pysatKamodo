```python
from pysat_kamodo.madrigal import Madrigal_Kamodo
```

```python
dmsp = Madrigal_Kamodo(
    '2001, 1, 1',
    user='firstname+lastname',
    password='email@address.com',
    platform='dmsp', name='ivm', tag='utd',
    inst_id='f12',
    regname_map = {'ni': 'n_i', 'ti': 't_i'},
    regname_replacements = {'+':'_plus', '-': '_minus'},
    default_stride=1,
    skip_variables=['year', 'month', 'day', 'hour', 'min']
    )
```

```python
dmsp
```

```python
dmsp.plot('t_i')
```
