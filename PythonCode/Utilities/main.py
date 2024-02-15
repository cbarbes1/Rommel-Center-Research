from utilities import Utilities
import json

def main():
    path_to_file = 'savedrecs.txt'
    output_dir = './split_files'
    
    utils = Utilities()
    
    file_paths = utils.make_files(path_to_file=path_to_file, output_dir=output_dir)
    
    # Save file_paths to a JSON file
    with open('file_paths.json', 'w') as fp:
        json.dump(file_paths, fp)
        
    # Print entries to ensure the right amount were made
    i = 0
    for entry, path in file_paths.items():
        print(f"Entry {entry} saved to: {path}")
        print(f"Entry Number: {i}")
        i += 1

def load_and_print_entry(entry_number):
    # Load file paths from the JSON file
    with open('file_paths.json', 'r') as fp:
        file_paths = json.load(fp)
        
    # Access and print the specified entry
    path = file_paths.get(str(entry_number)) # JSON keys are always strings
    
    if path:
        print(f"Entry: {entry_number} saved to: {path}")
    else:
        print(f"No entry found for number: {entry_number}")
      
if __name__ == "__main__":
    # If commented out, uncomment the below line if you need to run the script to make files again
    main()
    
    # If commented out, uncomment the line below to load and print a specific entry without rerunning the entire program
    #for i in range(1, 655):
     #   load_and_print_entry(i)
      #  print('\n')