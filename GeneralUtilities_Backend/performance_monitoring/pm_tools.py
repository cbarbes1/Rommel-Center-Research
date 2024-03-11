import time
import psutil


def monitor_system_resources():
    """Prints the current system's CPU and memory usage."""
    cpu_percent = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory()

    print(f"CPU Percent: {cpu_percent}%")
    print(f"Memory Usage: {memory_usage.used / (1024 ** 3):.2f} GB")


def get_system_resources():
    """Returns the current system's CPU and memory usage as a dictionary."""
    resources = {
        "cpu_percent": psutil.cpu_percent(),
        "memory_used_gb": psutil.virtual_memory().used / (1024**3),
    }
    return resources
