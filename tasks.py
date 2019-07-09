from celery import Celery
import time
import requests

app = Celery('tasks', broker='redis://localhost')

app.conf.worker_prefetch_multiplier = 10

@app.task
def add(x, y):
    # time.sleep(10)
    req = requests.get('http://dummy.restapiexample.com/api/v1/employees')
    return x+y