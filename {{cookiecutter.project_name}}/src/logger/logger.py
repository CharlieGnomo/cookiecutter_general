import logging
import sys
#APP_LOGGER_NAME = 'UC14'

def setup_app_level_logger(logger_name = APP_LOGGER_NAME, file_name=None): 
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)s - %(funcName)2s() - %(message)s")
    #mirar como escribir el nombre de la función
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.handlers.clear()
    logger.addHandler(stream_handler)
    if file_name:
        file_handler = logging.FileHandler(file_name)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger

def get_logger(module_name):    
    return logging.getLogger(APP_LOGGER_NAME).getChild(module_name)
