import os

directory = 'split_files'
txt_file_count = sum(1 for file in os.listdir(directory) if file.endswith('.txt'))

print(f"Number of .txt files in {directory}: {txt_file_count}")

# remove new line
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        
        with open(file_path, 'r') as file:
            content = file.read()
            
        if content.startswith('\n'):
            content = content[1:]
            
        with open(file_path, 'w') as file:
            file.write(content)
            
print("removed leading new line from all files")