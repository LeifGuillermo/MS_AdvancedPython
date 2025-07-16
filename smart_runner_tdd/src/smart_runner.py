import logging
import itertools
import time
from functools import wraps

log = logging.getLogger(__name__)


def unique_id_generator():
    """
    Generator for unique, sequential integer IDs.
    """
    yield from itertools.count(1)

_global_id_generator_instance = unique_id_generator()

# Decorator demo
def monitor_execution(func):
    """
    Decorator to log function execution details.

    Scoping: The 'wrapper' function forms a closure over 'func'
    from the decorator's outer-scope and '_global_id_generator_instance'
    from the module's global scope.
    'start_time', 'end_time', and 'duration' are all local to each call
    of 'wrapper'.
    """
    @wraps(func) # wraps allows python to see the original function's attributes rather than the wrapper's attributes when accessing the original function's attributes
    def wrapper(*args, **kwargs):
        current_id = next(_global_id_generator_instance)
        log.info(f"Unique ID: {current_id} - Executing {func.__name__}(args={args}, kwargs={kwargs})")
        start_time = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            log.error(f"Unique ID: {current_id} - {func.__name__} failed with: {e}")
            raise
        finally:
            end_time = time.perf_counter()
            duration = end_time - start_time
            log.info(f"Unique ID: {current_id} - Finished {func.__name__} in {duration:.4f} seconds.")
        return result
    return wrapper




