import flask
import prometheus_client as pc
import werkzeug as wz
import mariadb

app = flask.Flask(__name__)
REQUEST_COUNT = pc.Counter("http_requests_total", "Total HTTP Requests")

# app.wsgi_app = wz.DispatcherMiddleware(app.wsgi_app, {"/metrics": pc.make_wsgi_app()})

incomes = [{"description": "salary", "amount": 5000}]

conn = mariadb.connect(
    host="10.104.50.23",
    port=3306,
    user="root",
    password="p",
    database="my_database",
)


@app.route("/")
def home():
    return "2"


cur = conn.cursor()


@app.route("/index")
def index():
    animals_result = ""
    cur.execute("SELECT * FROM Animals", animals_result)
    return f"Connected to database: {animals_result}"


@app.route("/app_metrics")
def metrics():
    return "REQUEST_COUNT"


@app.route("/incomes", methods=["POST"])
def add_income():
    incomes.append(flask.request.get_json())
    return incomes
