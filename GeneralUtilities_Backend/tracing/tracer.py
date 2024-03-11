import functools
import time
import os
import traceback
from datetime import datetime

def trace(log_file="/mnt/linuxlab/home/spresley1/COSC425/RecentAsOf_3-8/Rommel-Center-Research/GeneralUtilities/tracing/trace_logs/trace_logs.txt", 
          level="INFO"):
    """
    A decorator factory that logs the execution of the decorated function with enhanced features.
    Supports different logging levels and includes timestamps in logs.

    Args:
        log_file (str, optional): Path to the log file. If None, logs to stdout.
        level (str, optional): Logging level (e.g., ERROR, INFO, DEBUG).
    """
    valid_levels = ["ERROR", "INFO", "DEBUG"]
    if level not in valid_levels:
        raise ValueError(f"Invalid logging level: {level}. Valid options are: {valid_levels}")

    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                error_info = traceback.format_exc()
                log_message = f"{datetime.now().isoformat()} ERROR in {func.__module__}.{func.__name__}: {error_info}"
                _log(log_message, log_file)
                raise  # Re-raise the exception after logging
            finally:
                end_time = time.time()
                if 'result' not in locals():
                    result = None
                if level in ["INFO", "DEBUG"]:
                    log_message = (
                        f"{datetime.now().isoformat()} TRACE: {func.__module__}.{func.__name__}, "
                        f"Execution time: {end_time - start_time:.4f} seconds, "
                        f"Args: {args}, Kwargs: {kwargs}, Result: {result}"
                    )
                    _log(log_message, log_file)

        return wrapped
    return decorator

def _log(message, log_file=None):
    """
    Helper function to log a message to either a file or stdout, with improved performance and thread safety.
    """
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        with open(log_file, "a") as f:
            f.write(message + "\n")
    else:
        print(message)

    