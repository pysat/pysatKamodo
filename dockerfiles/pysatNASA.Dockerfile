FROM pysat_kamodo:latest

RUN git clone https://github.com/pysat/pysatNASA.git
RUN pip install pysatNASA