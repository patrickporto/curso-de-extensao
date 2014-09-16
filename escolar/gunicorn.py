import multiprocessing

reload = True
bind = "127.0.0.1:9000"
workers = multiprocessing.cpu_count() * 2 + 1
chdir = "/opt/app"
pythonpath = "/opt/env/lib/python3.4/site-packages"