"""
Logging demo 1
Logging levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging

# logging.warning("warning message")
# logging.info("this is an info message")
# logging.debug("this is a debug message")
# logging.error("error message here")

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.warning("warning message")
logging.info("this is an info message")
logging.debug("this is a debug message")
logging.error("error message here")