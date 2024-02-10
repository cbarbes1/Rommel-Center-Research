from utilities import utilities
import json

def main():
    path_to_file = 'savedrecs.txt'
    output_dir = './split_files'
    
    utils = utilities()
    
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
        
if __name__ == "__main__":
    main()
    
    # uncomment the line below to load and print a specific entry without rerunning the entire program
    # load_and_print_entry(1)