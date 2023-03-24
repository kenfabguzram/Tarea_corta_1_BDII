import flask
import prometheus_client as pc
import werkzeug as wz
import mariadb
import json

app = flask.Flask(__name__)
REQUEST_COUNT = pc.Counter("http_requests_total", "Total HTTP Requests")

# app.wsgi_app = wz.DispatcherMiddleware(app.wsgi_app, {"/metrics": pc.make_wsgi_app()})

conn = mariadb.connect(
    host="10.101.19.96",
    port=3306,
    user="my_user",
    password="p",
    database="my_database",
)


@app.route("/", methods=["GET"])
def home():
    return "2"


cur = conn.cursor()


@app.route("/mariadb/get", methods=["GET"])
def mariadb_get():
    json_input = flask.request.get_json()
    query = json_input["query"]
    try:
        cur.execute(query)

        row_headers = [x[0] for x in cur.description]
        json_data = []
        for result in cur:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)
    except mariadb.Error as e:
        return f"Error: {e}"


@app.route("/mariadb/post", methods=["POST"])
def mariadb_post():
    json_input = flask.request.get_json()
    query = json_input["query"]
    try:
        cur.execute(query)
    except mariadb.Error as e:
        return f"Error: {e}"


@app.route("/app_metrics")
def metrics():
    return "REQUEST_COUNT"
