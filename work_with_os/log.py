import logging
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

logFile = 'test.log'

my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=1*1024*1024, 
                                 backupCount=1, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)

app_log = logging.getLogger('root')
app_log.setLevel(logging.INFO)

app_log.addHandler(my_handler)

n = 0
while True:
    n += 1
    app_log.info("data {}".format(n))
