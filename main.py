import shutil
import os

# Define source and destination paths
source_path = os.path.join(os.path.expanduser('~'), 'Downloads')
doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
video_path = os.path.join(os.path.expanduser('~'), 'Videos')
picture_path = os.path.join(os.path.expanduser('~'), 'Pictures')
exe_path = os.path.join(source_path, 'Programs')
other_path = os.path.join(source_path, 'Miscellaneous')
zip_path = os.path.join(source_path, 'Program Setup')

# Dictionary to map file extensions to their corresponding paths
file_type_paths = {
    '.pdf': doc_path,
    '.mp4': video_path,
    '.avi': video_path,
    '.mkv': video_path,
    '.exe': exe_path,
    '.zip': zip_path,
    '.rar': zip_path,
    '.tar.gz': zip_path,
    '.jpg': picture_path,
    '.jpeg': picture_path,
    '.png': picture_path,
    '.lnk': exe_path
}


# Function to relocate files to the appropriate directory
def relocate_files(relocate_path):
    destination_path = os.path.join(relocate_path, file)
    print(destination_path)
    shutil.move(full_file_path, destination_path)
    print(f"File moved to: {destination_path}")


# Iterate over each file in the source directory
for file in os.listdir(source_path):
    full_file_path = os.path.join(source_path, file)

    # Skip directories
    if os.path.isdir(full_file_path):
        continue

    # Get file extension
    _, file_extension = os.path.splitext(file)

    # Determine the relocation path based on the file extension
    relocate_path = file_type_paths.get(file_extension, other_path)

    # Move the file to the appropriate directory
    relocate_files(relocate_path)
