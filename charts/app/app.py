from flask import Flask
from prometheus_client import Counter, generate_latest
from flask import Response

app = Flask(__name__)
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')

@app.route('/')
def hello_world():
    REQUEST_COUNT.inc()
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    return Response(generate_latest(REQUEST_COUNT), mimetype='text/plain')