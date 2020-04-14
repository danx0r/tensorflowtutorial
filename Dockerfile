#FROM 763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-training:2.1.0-gpu-py36-cu101-ubuntu18.04
FROM eye0/datahub:awscu10.1tf

RUN apt-get update
RUN apt-get install -y nano ipython3

WORKDIR /root
COPY entrypoint.sh .
COPY beginner.py .
COPY beginner.ipynb .
COPY ssh_keys.txt .ssh/

RUN cat .ssh/ssh_keys.txt >> .ssh/authorized_keys

ENTRYPOINT ["/root/entrypoint.sh"]
