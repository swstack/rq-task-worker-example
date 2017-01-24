from redis import Redis
from rq import Queue, Connection
from tasks import tick
import time

redis_connection = Redis('localhost', 6379)
# redis_connection = redis.from_url('redis://localhost:6379')

default_queue = Queue(connection=redis_connection)

default_queue.enqueue(tick, 'task 1')
time.sleep(1)
default_queue.enqueue(tick, 'task 2')
