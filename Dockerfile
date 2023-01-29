FROM python:3.10

WORKDIR /app/

COPY . /app/
COPY ./requirements.txt /app/

RUN pip install -r requirements.txt
########################## 필수 ##
RUN export MYSQL_URL=
#################################
CMD uvicorn --port 8000 main:app
