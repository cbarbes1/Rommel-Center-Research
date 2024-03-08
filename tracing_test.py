from GeneralUtilities.tracing.tracer import trace


@trace(log_file="/mnt/linuxlab/home/spresley1/COSC425/RecentAsOf_3-8/Rommel-Center-Research/complex_test_log.txt", level="DEBUG")
def process_user_data(raw_data):
    """Validates and processes raw user data."""
    if not isinstance(raw_data, dict) or 'age' not in raw_data or 'name' not in raw_data:
        raise ValueError("Invalid user data. Must be a dict with 'age' and 'name'.")
    processed_data = {"name": raw_data["name"].strip(), "age": int(raw_data["age"])}
    return processed_data

@trace(log_file="/mnt/linuxlab/home/spresley1/COSC425/RecentAsOf_3-8/Rommel-Center-Research/complex_test_log.txt", level="DEBUG")
def perform_calculations(data):
    """Performs complex calculations on the data."""
    if data["age"] <= 0:
        raise ValueError("Age must be greater than 0.")
    result = 100 / data["age"]  # Could fail with division by zero
    return result

@trace(log_file="/mnt/linuxlab/home/spresley1/COSC425/RecentAsOf_3-8/Rommel-Center-Research/complex_test_log.txt", level="DEBUG")
def update_database(result):
    """Simulates updating a database with the result."""
    print(f"Updating database with result: {result}")
    # Simulate a database operation that could fail
    if result > 5:
        raise Exception("Database update failed due to high result value.")

# Main block to simulate the process and catch potential errors
if __name__ == "__main__":
    raw_user_data = [{"name": "Alice ", "age": "30"}, {"name": "Bob", "age": "0"}, {"name": "Charlie", "age": "-5"}]
    
    for user_data in raw_user_data:
        try:
            processed_data = process_user_data(user_data)
            calculation_result = perform_calculations(processed_data)
            update_database(calculation_result)
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Check the detailed log for more information.")

    print("\nSimulation complete. Check 'complex_test_log.txt' for detailed execution logs.")
