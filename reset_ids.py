import os
import glob
import re
import sys

def remove_unwanted_lines(directory):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return
    
    # Regex to match lines <!--ID: any integers-->
    pattern = re.compile(r'<!--ID:\s*\d+-->')
    
    path_pattern = os.path.join(directory, '*.md')
    
    md_files = glob.glob(path_pattern)
    
    if not md_files:
        print("No *.md files found in the directory.")
        return

    for file_name in md_files:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        new_lines = [line for line in lines if not pattern.search(line)]
        
        with open(file_name, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)
    
    print("Processing complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 remove_ids.py <folder_path>")
    else:
        directory_path = sys.argv[1]
        remove_unwanted_lines(directory_path)
