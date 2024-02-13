FROM python:3.8

WORKDIR /app

COPY backend/ .

RUN pip install mysql mysql-connector-python mysqlclient PyMySQL

CMD ["python", "server.py"]