import logging

fileName = '/home/ubuntu/mySite/util/logs'

class Log():
    def __init__(self,name):
	f = '%(asctime)s - %(name)s(%(lineno)d) [%(levelname)s] - %(message)s'
	self.logger = logging.getLogger(name )
 	formatter = logging.Formatter(f)
	console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
 	console.setFormatter(formatter)

        self.logger.addHandler(console)
        self.logger.setLevel(logging.DEBUG)
        logging.basicConfig(level=logging.ERROR,
                        format=f,
                        filename=fileName,
                        )
   
def main():
    myLog = Log('test').logger
    
    myLog.info('testmsg')
    myLog.debug('testmsg')
    myLog.warning('testmsg')
    myLog.error('testmsg')
    myLog.critical('testmsg')

if __name__ == '__main__':
    main()
