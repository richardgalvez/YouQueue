ARG PYTHON_VERSION=3.14.2

FROM python:${PYTHON_VERSION}-alpine3.23

RUN apk update && apk upgrade

WORKDIR /server

COPY ./requirements.txt /server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

COPY . /server

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
