FROM python:3.8

WORKDIR /app

COPY backend/server.py .

RUN pip install mysql-connector-python

CMD ["python", "server.py"]