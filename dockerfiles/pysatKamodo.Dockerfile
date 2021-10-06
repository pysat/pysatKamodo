FROM pysat


RUN git clone https://github.com/EnsembleGovServices/kamodo-core.git
RUN pip install -e kamodo-core

# Keep plotly at lower api
RUN pip install plotly==4.7.1

COPY . /pysatKamodo
RUN pip install -e pysatKamodo

RUN conda install -c conda-forge jupytext jupyter

WORKDIR /pysatKamodo

# CMD ["kamodo-serve"]
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
