FROM python:3.10

WORKDIR /app/

COPY . /app/
COPY ./requirements.txt /app/

RUN pip install -r requirements.txt && export MYSQL_URL=mysql+aiomysql://admin:o815o511@database-2.cwwalfzheezp.ap-northeast-2.rds.amazonaws.com:3306/jiseong2?charset=UTF8MB4

CMD uvicorn --host=127.0.0.1 --port 80 main:app
