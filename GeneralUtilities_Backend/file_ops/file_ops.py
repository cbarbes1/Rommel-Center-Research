import csv
import json
import os


class FileOps:
    def __init__(self, output_dir=None):
        self.output_dir = output_dir

    def read_file(self, file_path, encoding="utf-8"):
        """Reads and returns the content of a file."""
        try:
            with open(file_path, "r", encoding=encoding) as file:
                return file.read()
        except Exception as e:
            print(f"An error occurred while reading {file_path}: {e}")
            return None

    def write_file(self, file_path, content, encoding="utf-8"):
        """Writes content to a file."""
        try:
            with open(file_path, "w", encoding=encoding) as file:
                file.write(content)
        except Exception as e:
            print(f"An error occurred while writing to {file_path}: {e}")

    def verify_output_dir(self):
        """Ensures the output directory exists, creating it if necessary."""
        try:
            if self.output_dir and not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir, exist_ok=True)
        except Exception as e:
            print(
                f"An error occurred while verifying/creating the output directory: {e}"
            )

    def read_json(self, file_path):
        """Reads and returns data from a JSON file"""
        try:
            with open(file_path, "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except Exception as e:
            print(f"An error occurred while reading JSON from {file_path}: {e}")
            return None

    def write_json(self, file_path, data, exclude_keys=None):
        """
        Writes a Python dictionary to a JSON file, excluding specified keys.

        Args:
            file_path (str): The path to the JSON file to be written.
            data (dict): The data to write to the JSON file.
            exclude_keys (str, list): A key or list of keys to exclude from the JSON output.
        """
        try:
            self.verify_output_dir()
            if isinstance(exclude_keys, str):
                exclude_keys = [exclude_keys]
            if exclude_keys:
                data = {
                    key: value for key, value in data.items() if key not in exclude_keys
                }
            with open(file_path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4)
        except Exception as e:
            print(f"An error occurred while writing JSON to {file_path}: {e}")

    def read_csv(self, file_path, delimiter=","):
        """Reads a CSV file and returns a list of dictionaries."""
        try:
            with open(file_path, mode="r", encoding="utf-8") as csvfile:
                return list(csv.DictReader(csvfile, delimiter=delimiter))
        except Exception as e:
            print(f"An error occurred while reading CSV from {file_path}: {e}")
            return None

    def write_csv(self, file_path, data, fieldnames, delimiter=","):
        """Writes a list of dictionaries to a CSV file."""
        try:
            self.verify_output_dir()
            with open(file_path, mode="w", newline="", encoding="utf-8") as csvfile:
                writer = csv.DictWriter(
                    csvfile, fieldnames=fieldnames, delimiter=delimiter
                )
                writer.writeheader()
                writer.writerows(data)
        except Exception as e:
            print(f"An error occurred while writing CSV to {file_path}: {e}")

    def read_large_files(self, file_path, encoding="utf-8"):
        """Generator to read a file line by line for memory efficiency."""
        try:
            with open(file_path, "r", encoding=encoding) as file:
                for line in file:
                    yield line
        except Exception as e:
            print(f"Error reading large file {file_path}: {e}")

    def read_large_json(self, file_path, encoding="utf-8"):
        """Generator to read a large json line by line for memory efficiency."""
        try:
            with open(file_path, "r", encoding=encoding) as file:
                for line in file:
                    yield json.loads(line)
        except Exception as e:
            print(f"Error reading large JSON file {file_path}: {e}")
