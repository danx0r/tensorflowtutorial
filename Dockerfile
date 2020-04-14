#FROM 763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-training:2.1.0-gpu-py36-cu101-ubuntu18.04
FROM eye0/datahub:awscu10.1tf

RUN apt-get update
RUN apt-get install -y nano ipython3

WORKDIR /root
COPY beginner.py .
COPY beginner.ipynb .

RUN echo foo > bar

ENTRYPOINT ["bash"]
