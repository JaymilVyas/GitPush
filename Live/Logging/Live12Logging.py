import logging
logging.basicConfig(filename="MyLog1.log",level=logging.INFO)
logging.info("This is my very first code for logging")
logging.warning("This is a warning. It is severe information for the user")
logging.error("This is an error message from the system.")
l=[1,2,3]
for i in l:
    if i==2:
        logging.info(i)
        logging.warning("This is a warning message for the list function. You have ran this code multiple times.")

logging.shutdown()
logging.error("Shutdown message??")
