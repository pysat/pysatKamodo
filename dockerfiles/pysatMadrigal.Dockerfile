FROM pysat_kamodo:latest

# RUN git clone https://github.com/pysat/pysatMadrigal.git
RUN conda install h5py
RUN pip install pysatMadrigal