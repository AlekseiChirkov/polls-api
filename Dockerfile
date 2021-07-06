FROM python:3.8-alpine
MAINTAINER Aleksei Chirkov

ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY ./requirements.txt /requirements.txt
RUN . /venv/bin/activate
RUN python3 -m pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /src
WORKDIR /src
COPY src /src

RUN adduser -D user
USER user
