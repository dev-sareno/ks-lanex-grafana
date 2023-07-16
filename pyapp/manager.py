import random
import time
from prometheus_client import Summary


# Create a metric to track time spent and requests made.
PYAPP_SAMPLE_METRIC_NO_LABELS = Summary('pyapp_sample_metric_no_labels', 'Time spent processing API request')
PYAPP_SAMPLE_METRIC = Summary('pyapp_sample_metric', 'Time spent processing API request', ['path'])

# Method A: using decorator
# Decorate function with metric.
@PYAPP_SAMPLE_METRIC_NO_LABELS.time()
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
    PYAPP_SAMPLE_METRIC.labels('/api/slow').observe(time_taken)

    return f"I slept for {v} seconds!"


def get_fast():
    # Method B: manual
    # PROMETHEUS: start tracking time
    start = time.time()

    # actual logic
    response = 'This is fast responding API!'

    # PROMETHEUS: end tracking time
    time_taken = time.time() - start
    PYAPP_SAMPLE_METRIC.labels('/api/fast').observe(time_taken)

    return response

