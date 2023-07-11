from flask import Flask
from prometheus_client import start_http_server
import manager


app = Flask(__name__)


def get_base():
    return "Hello, World!"

@app.route("/")
def hello():
    return manager.get_hello()


@app.route("/api/slow")
def slow():
    return manager.get_slow()


if __name__ == "__main__":
    # Start up the server to expose the metrics.
    start_http_server(9090)
    app.run(debug=False, host="0.0.0.0", port=8001)
