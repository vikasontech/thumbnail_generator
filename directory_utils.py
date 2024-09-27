import os

import zipfile
import subprocess

# Create the directory
def create_dir(directory_name):
    try:
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def list_files_in_directory(directory_path):
    try:
        # List all files in the specified directory
        files = os.listdir(directory_path)
        print(f"Files in '{directory_path}':")
        # for file in files:
        #     # Check if it's a file (not a directory)
        #     if os.path.isfile(os.path.join(directory_path, file)):
        #         print(file)
        return list(filter(lambda file: os.path.isfile(os.path.join(directory_path, file)) , files))   
    except Exception as e:
        print(f"Error: {e}")
    return []

def separate_file_name_and_extension(file_path):
    # Get the file name and extension
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    return file_name, file_extension

# def unzip_dir(zip_file_name):
#     # Specify the path to the ZIP file and the extraction directory
#     # zip_file_path = 'path/to/your/file.zip'
#     extraction_directory =  os.path.dirname(zip_file_name)
#     if (not os.path.isfile(zip_file_name)):
#         raise ValueError(zip_file_name +" is not a valid zip file.")

   
#     # Create the extraction directory if it doesn't exist
#     os.makedirs(extraction_directory, exist_ok=True)

#     # Unzip the file
#     with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
#         zip_ref.extractall(extraction_directory)

#     print(f"Extracted all files to '{extraction_directory}'")
#     return extraction_directory;

# def flat_dir(extraction_directory):
#     # Create a temporary directory
#     with temp_file.TemporaryDirectory() as temp_dir:
#         print(f"Temporary directory created at: {temp_dir}")
                
#         # Define the command as a list of arguments
#         command = ["ls", "-l"]  # Example: listing files in long format

#         # Run the command
#         result = subprocess.run(command, capture_output=True, text=True)

#         # You can use the temporary directory here
#         # Example: create a file in the temp directory
#         temp_file_path = os.path.join(temp_dir, 'temp_file.txt')
#         with open(temp_file_path, 'w') as temp_file:
#             temp_file.write("This is a temporary file.")

#         # The temp_dir and its contents will be cleaned up automatically when exiting the with block

#         # find "$SOURCE_DIR" -type f -exec mv {} "$TARGET_DIR" \;