FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /wallet_system
WORKDIR /wallet_system
COPY ./wallet_system /wallet_system

EXPOSE 8000

RUN adduser -disabled-login user
USER user