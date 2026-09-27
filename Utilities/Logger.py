import logging

class log_generator_class:
    @staticmethod
    def loggen_method():
        log_file = logging.FileHandler(".\\Logs\\Credkart_logging.log")
        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s")
        log_file.setFormatter(log_format)
        logger = logging.getLogger()
        logger.addHandler(log_file)
        logger.setLevel(logging.ERROR)
        return logger
