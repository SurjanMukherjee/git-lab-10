import os
import shutil

# Q1: Print current working directory
print("Current Working Directory:", os.getcwd())

# Q2: Check if a path is a file or directory
path = os.getcwd()  # You can change this to test other paths
if os.path.isfile(path):
    print(f"{path} is a file.")
elif os.path.isdir(path):
    print(f"{path} is a directory.")
else:
    print(f"{path} does not exist.")

# Q3: Create a directory (if not exists)
folder_name = "test_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created folder: {folder_name}")
else:
    print(f"Folder already exists: {folder_name}")

# Q4: List only .txt files in current directory
txt_files = [f for f in os.listdir() if f.endswith(".txt") and os.path.isfile(f)]
print("Text files in current directory:", txt_files)

# Q5: Main task
reports_dir = "reports"

# Step 1: Check/create reports directory
if not os.path.exists(reports_dir):
    os.mkdir(reports_dir)
    print(f"Created directory: {reports_dir}")
else:
    print(f"Directory already exists: {reports_dir}")

# Step 2: List all .txt files in current directory
txt_files = [f for f in os.listdir() if f.endswith(".txt") and os.path.isfile(f)]

# Step 3: For each .txt file
for file in txt_files:
    print(f"Processing file: {file}")
    # Move file into reports directory
    shutil.move(file, os.path.join(reports_dir, file))
    print(f"Moved {file} to {reports_dir}")