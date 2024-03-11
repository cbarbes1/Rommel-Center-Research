import logging
import os


def configure_logger(
    name, log_file=None, level=logging.DEBUG, enable_console_logging=True
):
    """Configures and returns a logger with both file and optional console handlers.

    Parameters:
    - name (str): Name of the logger.
    - log_file (str, optional): Path to the log file. Defaults to 'log_file.txt' in the current working directory.
    - level (logging.LEVEL, optional): Logging level, e.g., logging.DEBUG, logging.INFO.
    - enable_console_logging (bool, optional): If True, logs will also be printed to the console. Default is True.

    Returns:
    - logging.Logger: Configured logger with specified settings.
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Ensure the logger has no duplicate handlers if function is called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    # Set up file logging
    if log_file is None:
        log_file = os.path.join(os.getcwd(), "log_file.txt")
    fh = logging.FileHandler(log_file)
    fh.setLevel(level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Set up console logging if enabled
    if enable_console_logging:
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
