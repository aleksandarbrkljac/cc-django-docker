FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ENV LAST_MODIFED=15:70
COPY . /app

EXPOSE 8000
RUN chmod +x /app/skripta.sh

ENTRYPOINT [ "/app/skripta.sh" ]


