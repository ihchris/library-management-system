import logging
from functools import wraps

# Configures the logger only once
logging.basicConfig(
    filename='library.log',  # or use 'console' with StreamHandler
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"➡️ Entering: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"✅ Exiting: {func.__name__}")
            return result
        except Exception as e:
            logging.exception(f"❌ Exception in {func.__name__}: {e}")
            raise  # Propagates the error to avoid hiding critical bugs
    return wrapper
