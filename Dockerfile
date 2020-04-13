#FROM 763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-training:2.1.0-gpu-py36-cu101-ubuntu18.04
FROM eye0/datahub:awscu10.1tf

COPY beginner.py .
COPY beginner.ipynb .

ENTRYPOINT ["bash"]
