FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Prevents Python from writing pyc files to disc (equivalent to python -B option)
#ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
#ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
#COPY . ./app
COPY ./app /app
COPY ./tests /tests
WORKDIR /app

COPY ./entrypoint.sh /
# default port is 8000
EXPOSE 80
ENTRYPOINT [ "sh","/entrypoint.sh" ]
