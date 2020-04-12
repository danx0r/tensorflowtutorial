FROM buildpack-deps:bionic

run apt-get update

RUN apt-get install -y virtualenv

RUN virtualenv venv -p python3

ENV PATH="venv/bin:$PATH"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY beginner.py .

ENTRYPOINT ["bash"]
