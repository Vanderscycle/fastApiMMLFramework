FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app

COPY ./entrypoint.sh /
# default port is 8000
EXPOSE 80
ENTRYPOINT [ "sh","/entrypoint.sh" ]
