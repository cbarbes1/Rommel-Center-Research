
---

# Logger Configuration Utility

The `configure_logger` utility function facilitates setting up a logger for Python applications. It provides customization for logging levels, formats, and outputs to both a file and optionally to the console.

## Usage

```python
configure_logger(name, log_file=None, level=logging.DEBUG, enable_console_logging=True)
```

### Parameters

- **name** (`str`): Name of the logger. Typically, the module or component name.
- **log_file** (`str`, optional): Path to the log file. Defaults to `log_file.txt` in the current working directory.
- **level** (`logging.LEVEL`, optional): Logging level threshold. Defaults to `logging.DEBUG`, for less info you can do `.INFO`, `.WARNING`, `.ERROR`, or `.CRITICAL`, each will have less output than the previous.
- **enable_console_logging** (`bool`, optional): If `True`, enables logging output to the console. Defaults to `True`.

### Returns

- **logger** (`logging.Logger`): A configured logger instance.

### Example

```python
import logging
from GeneralUtilities.logging.logger import logging

# Basic configuration with console output
logger = configure_logger('my_script')

# Configuration without console output
logger = configure_logger('my_script', enable_console_logging=False)

# Custom log file and level, with console output
logger = configure_logger('my_script', 'path/to/my_log.txt', level=logging.DEBUG)

# Use the logger
logger.info("Info message.")
logger.debug("Debug message.")
```

### Function Details

- **Log File**: Defaults to `log_file.txt` in the current working directory if not specified.
- **Log Format**: Includes timestamp, logger name, log level, and message.
- **Console Logging**: Optional. Controlled by `enable_console_logging`.
- **Directory Creation**: Automatically creates needed directories for the log file.

---