# This is a cheat sheet meant for the topic of logging
import logging
from logging import log

# We can log to 5 different levels of severity.

logging.debug('This is a debug message')
logging.info('This is an info message!')
logging.warning('This is a warning message!')
logging.error('This is an error message!')
logging.critical('This is a critical error message!')

# By default only the warning, error and critical messages are printed out in the output.
