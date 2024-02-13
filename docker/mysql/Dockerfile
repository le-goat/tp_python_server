FROM mysql:8.1.0

ENV MYSQL_ROOT_PASSWORD root

COPY ./mysql_scripts/schema.sql /docker-entrypoint-initdb.d/schema.sql
COPY ./mysql_scripts/privileges.sql /docker-entrypoint-initdb.d/privileges.sql