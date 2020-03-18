"""
Logger Demo
"""

import logging
import logging.config

class LoggerDemoConf():

    def testLog(self):
        # create logger
        logging.config.fileConfig('logging.conf')  # extension should be .conf
        logger = logging.getLogger(LoggerDemoConf.__name__)  # creating a logger object named LoggerDemoConf

        # logging messages
        logger.debug('debug messages')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')

demo = LoggerDemoConf()
demo.testLog()