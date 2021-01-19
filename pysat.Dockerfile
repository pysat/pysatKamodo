FROM continuumio/miniconda3:latest

# Borrowed from travis
RUN conda init bash

# RUN conda create -n pysat python==3.7
# SHELL ["conda", "run", "-n", "pysat", "/bin/bash", "-c"]
RUN conda install python==3.7
RUN conda install numpy scipy requests beautifulsoup4 lxml netCDF4 h5py nose pytest-cov pytest-ordering coveralls future

RUN conda install 'pandas>=0.23, <0.25'
RUN conda install 'xarray<0.15'
RUN conda install 'kiwisolver<1.2'

RUN pip install madrigalWeb
RUN pip install PyForecastTools

#  gfortran needed for pysatCDF
RUN apt-get install -y gfortran
RUN conda install -c conda-forge make
RUN pip install pysatCDF >/dev/null

# pysat itself
RUN pip install pysat
RUN mkdir -p /pysatData
RUN python -c "import pysat; pysat.utils.set_data_dir('/pysatData')"