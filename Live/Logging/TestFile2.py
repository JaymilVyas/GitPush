import logging
logging.basicConfig(filename="devidefunction1.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')
def devide(a,b):
    logging.info("the number entered by user is %s and %s", a, b)
    try:
        logging.info("We are into function")
        div=a/b
        logging.info("We have completed a division operations")
        logging.info("result of the code is %s ",div)
        return div
    except Exception as e:
        logging.exception(e)
devide(3,0)
print(devide(3,2))