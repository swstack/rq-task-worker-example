# Simple RQ worker process and client

Processes:

* `redis-server` - redis server
* `python src/worker.py` - worker process responsible for running queued tasks
* `python src/client.py` - example client enqueue'ing tasks
