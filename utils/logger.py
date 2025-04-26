import logging
from config.config import Config

def setup_logger():
    logger = logging.getLogger("BDDFramework")
    if not logger.handlers:  # Prevent duplicate handlers
        logger.setLevel(getattr(logging, Config.LOG_LEVEL))
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger 