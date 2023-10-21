FROM ubuntu:latest

COPY src ./src
COPY .env .
COPY poetry.lock .
COPY pyproject.toml .
RUN mkdir static
RUN apt-get update  \
    && apt-get install -y --no-install-recommends default-jre default-jdk
RUN javac -version

RUN apt-get install python3 -y  \
    && apt-get install python3-pip -y  \
    && apt-get install -y uvicorn
RUN apt install python-is-python3
RUN apt-get install golang -y
RUN go version

RUN pip install poetry
RUN poetry config virtualenvs.create false  \
    && poetry install
RUN chmod 777 -R /static
EXPOSE 9000

CMD ["python3", "-O", "-m", "src"]
