from rq import Queue, Connection, Worker
from redis import Redis

redis_connection = Redis('localhost', 6379)
# redis_connection = redis.from_url('redis://localhost:6379')


with Connection(redis_connection):
    default_queue = Queue()
    worker = Worker(default_queue)
    worker.work()
