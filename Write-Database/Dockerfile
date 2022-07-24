FROM python:3.8-slim-buster
RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python", "main.py"]