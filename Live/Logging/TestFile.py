import logging
logging.basicConfig(filename="MyLogFile2.log",level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')
logging.info("This is my 2nd log file with timestamp")
