
# Trace Decorator Utility

The `trace` utility function is a decorator designed to enhance debugging and logging. It wraps any function to log its execution details, including start time, end time, arguments, return values, and exceptions. It supports logging to both a file and optionally to the standard output.

## Usage

```python
@trace(log_file="path/to/log_file.txt", level="DEBUG")
def my_function(param1, param2):
    # Function implementation
```

### Parameters

- **log_file** (`str`, optional): Path to the log file. Defaults to `None`, which means logging will be directed to the standard output (stdout).
- **level** (`str`, optional): Specifies the logging level. Supports "ERROR", "INFO", and "DEBUG". Defaults to "INFO". Higher levels include more detailed logging.

### Decorated Function Parameters

- Any parameters accepted by the decorated function itself.

### Returns

- The return value of the decorated function is passed through unchanged.

### Example

```python
@trace(level="DEBUG")
def add(a, b):
    return a + b

# With log file
@trace(log_file="logs/my_app.log", level="INFO")
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero!")
    return a / b
```

### Function Details

- **Logging Output**: Includes a timestamp, function name, execution time, arguments, keyword arguments, and the function's result. In case of an exception, the error message is logged.
- **Log File Handling**: If a `log_file` path is provided, the utility ensures that the directory exists and appends logs to the file. If the path is `None`, logs are printed to stdout.
- **Debugging Support**: At the "DEBUG" level, detailed information, including stack traces for exceptions, is logged, aiding in the debugging process.
- **Thread Safety**: The logging implementation is designed to be thread-safe, allowing it to be used in multi-threaded environments without log message collision.
- **Performance Monitoring**: Logs the execution time of each call, helping identify performance bottlenecks.
