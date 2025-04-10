# In your gunicorn.conf.py
workers = 4  # Typically 2-4 x CPU cores
worker_class = 'gevent'  # For async I/O
worker_connections = 1000
timeout = 120  # Increase for debugging
graceful_timeout = 30
keepalive = 5  # Better for persistent connections