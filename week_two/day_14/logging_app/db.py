import logging

logger = logging.getLogger('logging_app.db')


def my_app():

    logger.debug("HERE IS DEBUG LOG")

    logger.info("HERE IS INFO LOG")

    logger.warning("HERE IS WARNING LOG")

    logger.error("HERE IS ERROR LOG")

    logger.critical("HERE IS CRITICAL LOG")
