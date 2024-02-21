FROM ubuntu:latest
LABEL authors="arche"

ENTRYPOINT ["top", "-b"]# This is our awesome docker file

FROM python:3-alpine3.17
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python3 ./hello.py