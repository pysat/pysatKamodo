FROM apembroke/pysat:latest


RUN git clone https://github.com/asherp/Kamodo.git
RUN pip install -e Kamodo

RUN git clone https://github.com/pysat/pysatKamodo.git
RUN pip install -e pysatKamodo

# RUN conda install jupyter

# CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]

WORKDIR pysatKamodo

CMD ["kamodo-serve"]


# WORKDIR Kamodo/readers/corhel
# ADD . pysatKamodo

# RUN pip install -e pysatKamodo