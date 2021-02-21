"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ


def max_workers():    
    return cpu_count() * 2 + 1


bind = '0.0.0.0:5500'
backlog = 2048
worker_class = 'sync'
workers = max_workers()

worker_connections = 1000
timeout = 100
keepalive = 2


#
#   Logging
#
#   logfile - The path to a log file to write to.
#
#       A path string. "-" means log to stdout.
#
#   loglevel - The granularity of log output
#
#       A string of "debug", "info", "warning", "error", "critical"
#
logfile = 'logs/dev.log'
errorlog = 'logs/error.log'
loglevel = 'debug'
accesslog = 'logs/access.log'
error_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
