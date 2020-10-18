FROM python:3.8-alpine

RUN apk add gcc musl-dev libffi-dev openssl-dev python3-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py main.py
CMD python3 main.py