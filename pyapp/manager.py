import random
import time
from prometheus_client import Summary


# Create a metric to track time spent and requests made.
GET_HELLO_REQUEST_TIME = Summary('get_hello_seconds', 'Time spent processing GET / request')
GET_SLOW_REQUEST_TIME = Summary('get_slow_seconds', 'Time spent processing GET /api/slow request')

# Method A: using decorator
# Decorate function with metric.
@GET_HELLO_REQUEST_TIME.time()
def get_hello():
    return "Hello, World!"


def get_slow():
    # Method B: manual
    # PROMETHEUS: start tracking time
    start = time.time()

    # actual logic
    v = random.randint(1, 5)
    time.sleep(v)

    # PROMETHEUS: end tracking time
    time_taken = time.time() - start
    GET_SLOW_REQUEST_TIME.observe(time_taken)

    return f"I slept for {v} seconds!"

