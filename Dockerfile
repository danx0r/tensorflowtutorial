#FROM nvidia/cuda:10.1-runtime-ubuntu18.04
FROM 763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-training:2.1.0-gpu-py36-cu101-ubuntu18.04

#RUN apt-get update

#RUN apt-get -y install python3 ipython3 python3-pip

#RUN pip3 install tensorflow

ENTRYPOINT ["bash"]
