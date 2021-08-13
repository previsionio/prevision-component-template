FROM python

RUN apt-get update && apt-get upgrade -y

COPY requirements.txt /requirements.txt
RUN python -m pip install -r /requirements.txt

COPY . /
