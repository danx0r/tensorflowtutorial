FROM buildpack-deps:bionic

run apt-get update

RUN apt-get install -y virtualenv

RUN virtualenv venv -p python3

ENV PATH="venv/bin:$PATH"

RUN pip install mido

ENTRYPOINT ["bash"]
