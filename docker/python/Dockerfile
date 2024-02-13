FROM python:3.8

WORKDIR /app

COPY backend/ .

RUN pip install mysql-connector-python

# Ajouter ces deux lignes pour exécuter dbCreator.py et tableCreator.py avant de lancer server.py
RUN python dbCreator.py
RUN python tableCreator.py

CMD ["python", "server.py"]