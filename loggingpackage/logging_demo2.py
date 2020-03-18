import logging
import loggingpackage.custom_logger as cl

class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):  # makes a new file called LoggingDemo2 (class name)
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warning message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        m2Log = cl.customLogger(logging.INFO) # makes a new file called method2.log (method name)
        m2Log.debug('debug message')
        m2Log.info('info message')
        m2Log.warning('warning message')
        m2Log.error('error message')
        m2Log.critical('critical message')

    def method3(self):
        m3Log = cl.customLogger(logging.INFO) # takes the method name instead of the class name shown in other files
        m3Log.debug('debug message')
        m3Log.info('info message')
        m3Log.warning('warning message')
        m3Log.error('error message')
        m3Log.critical('critical message')


demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()