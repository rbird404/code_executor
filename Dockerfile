FROM ubuntu:latest

COPY src ./src
COPY ./pyproject.toml /pyproject.toml
COPY ./poetry.lock /poetry.lock

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

RUN mkdir -p /static
RUN chmod 777 -R /static

CMD ["python3", "-O", "-m", "src"]
