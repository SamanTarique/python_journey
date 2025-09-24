import logging

# logging.basicConfig(
#     filename='logger.log', filemode='a',
#     format='%(name)s - %(levelname)s - %(message)s',
#     level=logging.DEBUG 
#     )

logging.basicConfig(
    filename='logger.log',
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
"""this ensures the logging level , if level is warning """
"""then the logs of warning and upper level will log in the file"""

logging.debug("This is a debug log")
logging.info("This is a info log")
logging.warning("This is a warning log")
logging.error("This is a error log")
logging.critical("This is a critical log")
