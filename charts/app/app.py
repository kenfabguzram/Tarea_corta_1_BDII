import flask
import prometheus_client as pc
import werkzeug as wz
import mariadb
import json
import pymongo as mongo


app = flask.Flask(__name__)
REQUEST_COUNT = pc.Counter("http_requests_total", "Total HTTP Requests")
# MARIADB_HOST = ""
# MARIADBGALERA_HOST = ""
# MONGODB_HOST = ""
# POSTGRESQL_HOST = ""
# POSTGRESQLHA_HOST = ""

# app.wsgi_app = wz.DispatcherMiddleware(app.wsgi_app, {"/metrics": pc.make_wsgi_app()})

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
            return json.dumps(json_data)
        else:

            return str(result)
    except mariadb.Error as e:
        return f"Error: {e}"


# # MariaDB-Galera --------------------------------------------------------------
# def get_mariadb_galera_cursor(host_ip: str):
#     mariadb_galera_connection = mariadb.connect(
#         host=host_ip,
#         port=3306,
#         user="my_user",
#         password="p",
#         database="my_database",
#     )
#     return mariadb_galera_connection.cursor()


# @app.route("/mariadb-galera/get", methods=["GET"])
# def mariadb_galera_get():
#     json_input = flask.request.get_json()
#     query = json_input["query"]
#     host_ip = json_input["host"]
#     try:
#         mariadb_galera_cursor = get_mariadb_galera_cursor(host_ip)
#         if mariadb_galera_cursor is None:
#             return "Error: please check the host ip and try again"
#         mariadb_galera_cursor.execute(query)

#         row_headers = [x[0] for x in mariadb_galera_cursor.description]
#         json_data = []
#         for result in mariadb_galera_cursor:
#             json_data.append(dict(zip(row_headers, result)))
#         return json.dumps(json_data)
#     except mariadb.Error as e:
#         return f"Error: {e}"


# @app.route("/mariadb-galera/post", methods=["POST"])
# def mariadb_galera_post():
#     json_input = flask.request.get_json()
#     query = json_input["query"]
#     host_ip = json_input["host"]
#     try:
#         mariadb_galera_cursor = get_mariadb_galera_cursor(host_ip)
#         if mariadb_galera_cursor is None:
#             return "Error: please check the host ip and try again"
#         mariadb_galera_cursor.execute(query)
#         row_headers = [x[0] for x in mariadb_galera_cursor.description]
#         json_data = []
#         for result in mariadb_galera_cursor:
#             json_data.append(dict(zip(row_headers, result)))
#         return json.dumps(json_data)
#     except mariadb.Error as e:
#         return f"Error: {e}"


# MongoDB -------------------------------------------------------------------
def mongo_insert(host_ip: str, animals_to_insert: list):
    # Set up a MongoDB client
    connection_string = f"mongodb://{host_ip}:27017/my_database"
    client = mongo.MongoClient(connection_string)
    db = client["my_database"]
    collection = db["animales"]
    return collection.insert_many(animals_to_insert)
    # return db.list_collection_names()


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
