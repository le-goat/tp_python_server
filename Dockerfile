FROM mysql:latest

COPY ./mysql-scripts/ /docker-entrypoint-initdb.d/
