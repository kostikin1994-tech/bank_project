import logging

def log(filename=None):
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO)
    else:
        logging.basicConfig(level=logging.INFO)

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logging.error(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                raise e
        return wrapper
    return decorator

