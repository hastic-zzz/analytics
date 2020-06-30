# Hastic analytics

Python service which gets tasks from [hastic-server-node](https://github.com/hastic/hastic-server/tree/master/server) like

* train statistical models
* detect patterns in time series data

See more 

## Arhitecture

Analytics gets tasks by websockets tasks asynchoriously, then launches threads in [actors with zmq messaging](https://github.com/hastic/analytics/blob/master/analytics/utils/concurrent.py)
* [asyncio](https://docs.python.org/3/library/asyncio.html)
* [concurrency](https://docs.python.org/3.6/library/concurrent.futures.html#module-concurrent.futures)
* [pyzmq](https://pyzmq.readthedocs.io/en/latest/)
* [websockets](https://github.com/aaugustin/websockets)
