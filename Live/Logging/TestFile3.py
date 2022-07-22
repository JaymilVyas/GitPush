import logging
logging.basicConfig(filename="LogFile3.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(message)s')

try:
    logging.info("I am trying to read the file with the name 'Jimmmy'")
    with open("Jimmy.txt","r"):
        logging.info("succesfully it has read the file ")
except Exception as e:
    logging.critical("this is a situation for us ")
    logging.error(e)
    logging.exception(e)
