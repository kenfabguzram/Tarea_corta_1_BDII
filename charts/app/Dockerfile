FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN apt install wget
RUN wget https://r.mariadb.com/downloads/mariadb_repo_setup
RUN echo "ad125f01bada12a1ba2f9986a21c59d2cccbe8d584e7f55079ecbeb7f43a4da4  mariadb_repo_setup" \
    | sha256sum -c -
RUN chmod +x mariadb_repo_setup
RUN ./mariadb_repo_setup \
    --mariadb-server-version="mariadb-10.6"
RUN apt install libmariadb3 libmariadb-dev -y
RUN apt-get install libpq-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]
