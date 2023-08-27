import os
import shutil

# Source directories for .jpg and .txt files
jpg_source_directory = '/Users/madhuupadhyay/Downloads/project-2-at-2023-08-10-22-52-937b35e0/images/train'
txt_source_directory = '/Users/madhuupadhyay/Downloads/project-2-at-2023-08-10-22-52-937b35e0/labels'

# Destination directory where .txt files will be transferred
destination_directory = '/Users/madhuupadhyay/Downloads/project-2-at-2023-08-10-22-52-937b35e0/labels/train'

# List all .jpg files in the jpg source directory
jpg_files = [f for f in os.listdir(jpg_source_directory) if f.endswith('.jpg')]

# Create the destination directory if it doesn't exist
os.makedirs(destination_directory, exist_ok=True)

# Transfer corresponding .txt files
for jpg_file in jpg_files:
    txt_file = os.path.splitext(jpg_file)[0] + '.txt'
    src_txt_path = os.path.join(txt_source_directory, txt_file)
    dst_txt_path = os.path.join(destination_directory, txt_file)
    
    # Check if the corresponding .txt file exists
    if os.path.exists(src_txt_path):
        shutil.move(src_txt_path, dst_txt_path)
        print(f"Transferred {txt_file} to destination directory")

print("Transfer completed!")
