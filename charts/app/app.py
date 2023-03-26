import flask
import prometheus_client as pc
import werkzeug as wz
import mariadb
import json
import pymongo as mongo


app = flask.Flask(__name__)
REQUEST_COUNT = pc.Counter("http_requests_total", "Total HTTP Requests")

# MariaDB -------------------------------------------------------------------
def get_mariadb_cursor(host_ip: str):
    mariadb_connection = mariadb.connect(
        host=host_ip,
        port=3306,
        user="root",
        password="p",
        database="my_database",
    )
    mariadb_connection.autocommit = True
    return mariadb_connection.cursor()


@app.route("/", methods=["GET"])
def home():
    return "2"


@app.route("/mariadb/post", methods=["POST"])
def mariadb_post():
    json_input = flask.request.get_json()
    query = json_input["query"]
    host_ip = json_input["host"]
    try:
        mariadb_cursor = get_mariadb_cursor(host_ip)
        result = mariadb_cursor.execute(query)
        if result is not None:
            row_headers = [x[0] for x in mariadb_cursor.description]
            json_data = []
            for result in mariadb_cursor:
                json_data.append(dict(zip(row_headers, result)))
            return json.dumps(json_data), 200
        else:
            return str(result), 100
    except mariadb.Error as e:
        return f"Error: {e}", 300


# MongoDB -------------------------------------------------------------------
def mongo_insert(host_ip: str, animals_to_insert: list):
    connection_string = f"mongodb://{host_ip}:27017/my_database"
    client = mongo.MongoClient(connection_string)
    db = client["my_database"]
    collection = db["animales"]
    return collection.insert_many(animals_to_insert)


def mongo_find(host_ip: str):
    connection_string = f"mongodb://{host_ip}:27017/my_database"
    client = mongo.MongoClient(connection_string)
    db = client["my_database"]
    collection = db["animales"]
    result = collection.find({})
    return_list = []
    for document in result:
        return_list.append(str(document))
    return return_list


@app.route("/mongodb/post", methods=["POST"])
def mongo_post():
    json_input = flask.request.get_json()
    animals_to_insert = json_input["animales"]
    host_ip = json_input["host"]
    return str(mongo_insert(host_ip, animals_to_insert))


@app.route("/mongodb/get", methods=["GET"])
def mongo_get():
    json_input = flask.request.get_json()
    host_ip = json_input["host"]
    return str(mongo_find(host_ip))


# Metrics
@app.route("/app_metrics")
def metrics():
    return "REQUEST_COUNT"
