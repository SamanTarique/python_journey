import logging

import app
import db
import logic

"""Setting formatter for console"""
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter(
    '%(levelname)s - %(message)s'
)
console_handler.setFormatter(console_formatter)


global_log_formatter = logging.Formatter(
    '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s:%(message)s'
)


#####################################################################


"""setting up logging for console level """
app_logger = logging.getLogger('logging_app.app')
app_logger.setLevel(logging.DEBUG)

"""setting up logging for file level(to save in log file)"""
app_handler = logging.FileHandler('app_db_logic.log')
app_handler.setLevel(logging.INFO)
app_handler.setFormatter(global_log_formatter)

"""attaching logger to the console and file level handling"""
app_logger.addHandler(console_handler)
app_logger.addHandler(app_handler)


#####################################################################


db_logger = logging.getLogger('logging_app.db')
db_logger.setLevel(logging.DEBUG)

db_handler = logging.FileHandler('app_db_logic.log')
db_handler.setLevel(logging.WARNING)
db_handler.setFormatter(global_log_formatter)

db_logger.addHandler(db_handler)
db_logger.addHandler(console_handler)


#####################################################################

logic_logger = logging.getLogger('logging_app.logic')
logic_logger.setLevel(logging.DEBUG)

logic_handler = logging.FileHandler('app_db_logic.log')
logic_handler.setLevel(logging.ERROR)
logic_handler.setFormatter(global_log_formatter)

logic_logger.addHandler(logic_handler)
logic_logger.addHandler(console_handler)

#####################################################################

app.my_app()
db.my_app()
logic.my_app()
