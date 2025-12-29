ARG PYTHON_VERSION=3.14.2

# TODO: Change to bookworm full image for net tools to troubleshoot DB connection
FROM python:${PYTHON_VERSION}-alpine3.23

WORKDIR /server

COPY ./requirements.txt /server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

COPY . /server

CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "8000"]
