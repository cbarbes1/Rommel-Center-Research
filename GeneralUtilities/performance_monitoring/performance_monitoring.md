
---

## System Monitoring Utilities for Model Training

This documentation provides details on using system monitoring utilities specifically designed to assist in monitoring system resources like CPU and memory usage during model training.

### 1. `monitor_system_resources()`

**Purpose:** Prints the current CPU and memory usage to the console, which will likely be useful during long model training sessions to ensure the system is not overburdened, or hitting a bottleneck.

**Usage:**

```python
from GeneralUtilities.performance_monitoring.pm_tools import monitor_system_resources

# To monitor system resources during model training
monitor_system_resources()
```

**Output:**

- Displays the current CPU usage percentage.
- Shows the current memory usage in GB.

### 2. `get_system_resources()`

**Purpose:** Returns the current system's CPU and memory usage in a structured format, allowing for programmable checks or logging during model training phases.

**Usage:**

```python
from GeneralUtilities.performance_monitoring.pm_tools import get_system_resources

# To retrieve system resource usage as a dictionary during model training
resources = get_system_resources()
print(resources)
```

**Output:**

- A dictionary containing `'cpu_percent'` and `'memory_used_gb'`, representing the current CPU usage in percentage and memory usage in GB, respectively.

**Example Output:**

```python
{
    'cpu_percent': 5.2,  # Current CPU usage percentage
    'memory_used_gb': 1.75  # Current memory usage in GB
}
```

### Integration Guide

- Installation: Ensure the `psutil` library is installed (`pip install psutil`).
- Directly import and use these utility functions in your training scripts.
- No additional parameters are required, making these tools easy to use.

### Practical Applications

- **During Model Training:** Utilize `monitor_system_resources()` to get insight on system resource usage, potentially aiding in identify bottlenecks or overutilization issues.
- **Automated Monitoring:** Use `get_system_resources()` to programmatically monitor and log system usage over time, allowing for feeback on how to optimize training.

---