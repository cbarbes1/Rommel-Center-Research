
---

# File Operations Utility Class Documentation

The `FileOps` class provides a set of utilities for file handling. It simplifies tasks such as reading and writing plain text, JSON, and CSV files. It also has methods to allow for reading large files (plain text and JSON).

## How to import
```python
from GeneralUtilities.file_ops.file_ops import FileOps
```

## Initialization

```python
file_ops = FileOps(output_dir='path/to/output')
```

- `output_dir` (optional): Specifies the default directory for writing files. If not provided, files are saved to the current directory.

## Methods

### `read_file(file_path, encoding='utf-8')`

Reads and returns the content of a file.

- `file_path`: Path to the file.
- `encoding` (optional): File encoding, defaulting to `'utf-8'`.

### `write_file(file_path, content, encoding='utf-8')`

Writes content to a file.

- `file_path`: Path to the output file.
- `content`: Content to be written.
- `encoding` (optional): File encoding.

### `verify_output_dir()`

Ensures the specified output directory exists, creating it if necessary.

### `read_json(file_path)`

Reads a JSON file and returns its content as a Python dictionary.

- `file_path`: Path to the JSON file.

### `write_json(file_path, data, exclude_keys=None)`

Writes a Python dictionary to a JSON file, optionally excluding specified keys. If excluding one key it can be passed in as a string, if excluding multiple keys pass them in as a list.

- `file_path`: Path to the output JSON file.
- `data`: Dictionary to write.
- `exclude_keys` (optional): Key(s) to exclude from the output.

### `read_csv(file_path, delimiter=',')`

Reads a CSV file and returns a list of dictionaries, one per row.

- `file_path`: Path to the CSV file.
- `delimiter` (optional): Field delimiter, default is `','`.

### `write_csv(file_path, data, fieldnames, delimiter=',')`

Writes a list of dictionaries to a CSV file.

- `file_path`: Path to the output CSV file.
- `data`: List of dictionaries to write.
- `fieldnames`: List of field names for the CSV header.
- `delimiter` (optional): Field delimiter.

### `read_large_files(file_path, encoding='utf-8')`

Generator for reading a file line by line, optimizing for memory efficiency.

- `file_path`: Path to the file.
- `encoding` (optional): File encoding.

### `read_large_json(file_path, encoding='utf-8')`

Generator for reading a large JSON file line by line, optimizing for memory efficiency.

- `file_path`: Path to the JSON file.
- `encoding` (optional): File encoding.

## Usage Examples

Reading and writing a JSON file, excluding specific keys:

```python
data = file_ops.read_json('input.json')
file_ops.write_json('output.json', data, exclude_keys=['sensitive_information'])
```

Handling a CSV file:

```python
rows = file_ops.read_csv('input.csv')
# Process rows
file_ops.write_csv('output.csv', rows, fieldnames=['id', 'name', 'value'])
```

Processing a large text file line by line:

```python
for line in file_ops.read_large_files('large_file.txt'):
    print(line)
    # Process line
```