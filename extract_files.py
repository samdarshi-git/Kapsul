import os

def extract_files_content(folder_paths, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:
        # Iterate over each folder path
        for folder_path in folder_paths:
            if not os.path.exists(folder_path):
                print(f"Warning: Folder '{folder_path}' does not exist.")
                continue

            # Walk through the directory
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    # Get the full path of the file
                    file_path = os.path.join(root, file)
                    try:
                        # Open each file and read its content
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # Write file name and relative path
                        relative_path = os.path.relpath(file_path, folder_path)
                        output.write(f"File: {relative_path}\n")
                        output.write("="*50 + "\n")
                        output.write(content + "\n")
                        output.write("="*50 + "\n\n")
                    except Exception as e:
                        # Handle files that cannot be read (e.g., binary files)
                        output.write(f"Could not read file: {file_path} ({str(e)})\n")
                        output.write("="*50 + "\n\n")

if __name__ == '__main__':
    folder_paths = [
        r'C:\Users\parih\Documents\PlatformIO\Projects\pill_dispenser\include',
        r'C:\Users\parih\Documents\PlatformIO\Projects\pill_dispenser\src'
    ]  # Use raw string literals for absolute paths
    output_file = r'C:\Users\parih\Documents\PlatformIO\Projects\pill_dispenser\output.txt'  # Specify the output file path
    extract_files_content(folder_paths, output_file)
    print(f"Content extracted to {output_file}")
