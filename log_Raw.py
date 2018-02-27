#import logging
# from logging.handlers import RotatingFileHandler
#import logging, logging.handlers

#get the root logger
#logger = logging.getLogger("Rotating Log")
#set overall level to debug, default is warning for root logger
#logger.setLevel(logging.INFO)
#handler = logging.handlers.TimedRotatingFileHandler('/srv/runme/sample/Raw.txt',when='M',interval=1, backupCount=10)
#filelog.setLevel(logging.DEBUG)

import logging
import time
import sys

from logging.handlers import TimedRotatingFileHandler
 
#----------------------------------------------------------------------
def create_timed_rotating_log(path):
    """"""
    logger = logging.getLogger("Rotating Raw.txt ")
    logger.setLevel(logging.INFO)
 
    handler = TimedRotatingFileHandler(path,
                                       when="m",
                                       interval=1,
                                       backupCount=100)
    logger.addHandler(handler)
 
    for i in range(6):
        logger.info("This is a test!")
        time.sleep(75)

#----------------------------------------------------------------------
if __name__ == "__main__":
    log_file = "/srv/runme/" + sys.argv[1] + "/Raw.txt"
    # print(log_file)
    # log_file = "/srv/runme/sample/Raw.txt"
    create_timed_rotating_log(log_file)
