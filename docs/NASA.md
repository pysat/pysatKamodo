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

```python
import pandas as pd
```

```python
kcnofs.B_up(pd.DatetimeIndex(['2009-01-01 00:00:03', '2009-01-01 00:00:05']))
```

```python
fig = kcnofs.plot('B_up')
```

```python
fig
```

```python
import plotly.io as pio
pio.write_image(fig, "cnofs_B_up.svg", engine="kaleido")
```
