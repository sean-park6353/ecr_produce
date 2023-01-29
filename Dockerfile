FROM python:3.10

WORKDIR /app/

COPY . /app/
COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

CMD uvicorn --host=127.0.0.1 --port 80 main:app
