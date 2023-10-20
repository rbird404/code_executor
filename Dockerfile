# FROM python:3.10

# ENV DEBIAN_FRONTEND=noninteractive

FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends default-jre default-jdk
RUN javac -version

RUN apt-get install python3 -y
RUN apt-get install python3-pip -y


RUN apt-get install golang -y 
RUN go version

COPY . .

