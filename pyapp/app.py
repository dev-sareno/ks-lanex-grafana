from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
import manager


app = Flask(__name__)

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

def get_base():
    return "Hello, World!"

@app.route("/")
def hello():
    return manager.get_hello()


@app.route("/api/slow")
def slow():
    return manager.get_slow()


@app.route("/api/fast")
def fast():
    return manager.get_fast()
