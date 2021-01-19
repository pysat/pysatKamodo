FROM apembroke/pysat:latest


RUN git clone https://github.com/asherp/Kamodo.git
RUN pip install -e Kamodo

RUN git clone https://github.com/pysat/pysatKamodo.git
RUN pip install -e pysatKamodo

# WORKDIR Kamodo/readers/corhel
# ADD . pysatKamodo

# RUN pip install -e pysatKamodo