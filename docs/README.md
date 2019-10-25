# About

This project tracks development of the kamodo-pysat interface. While pysat focuses
on providing a unified way of retrieving, loading and cleaning instrument data,
Kamodo provides a math-oriented API for interpolation, function composition, 
and quick-look graphics. The combination of the two approaches simplifies 
the workflow for science users, while minimizing the effort needed for science discovery.

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
