import multiprocessing

# Server Socket
bind = 'unix:/var/run/otherbu_gunicorn.sock'
backlog = 2048

# Worker Processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
max_requests = 0
timeout = 30
keepalive = 2
debug = False
spew = False

preload_app = True
# daemon = True
pidfile = '/var/run/otherbu_gunicorn.pid'
# user = 'app1_app'
# group = 'nginx'
# umask = 0002

# Logging
# logfile = '/var/log/gunicorn/my_app.log'
# loglevel = 'info'
# logconfig = None

# Process Name
proc_name = 'otherbu_gunicorn'
