FROM python:3.10

ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update && apt-get install -y --no-install-recommends default-jre default-jdk

RUN javac -version

COPY . .

