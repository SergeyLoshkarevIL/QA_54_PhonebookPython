import logging


#DEBUG -> INFO -> WARNING -> ERROR-> CRITICAL
def configure_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename = "logs/test.log",
        filemode = "a"
    )