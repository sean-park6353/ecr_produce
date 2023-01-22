FROM python:3.10

WORKDIR /app/

COPY . /app/
COPY ./requirements.txt /app/

RUN pip install -r requirements.txt && apt-get update && apt-get install -y vim && apt-get install -y zsh
RUN MYSQL_URL='mysql+aiomysql://admin:o815o511@database-2.cwwalfzheezp.ap-northeast-2.rds.amazonaws.com:3306/jiseong2?charset=UTF8MB4'
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
RUN apt-get install -y fasd
CMD uvicorn --host=0.0.0.0 --port 8000 main:app
