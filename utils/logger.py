import logging
import os

def setup_logger(name):
    os.makedirs("logs", exist_ok=True)
    log_file = f"logs/{name}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger
