import random
from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/api/slow")
def slow():
    v = random.randint(1, 5)
    time.sleep(v)
    return f"I slept for {v} seconds!"
