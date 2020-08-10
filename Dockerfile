# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP "api/config:app"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

EXPOSE 5000

# CMD flask run --host=0.0.0.0
CMD python api/server.py --host=0.0.0.0
