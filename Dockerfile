FROM python

RUN apt-get update && apt-get upgrade -y

COPY requirements.txt /sample_n/requirements.txt
RUN python -m pip install -r /sample_n/requirements.txt

COPY . components/

# ENTRYPOINT python3 component/sample/src/sample.py
