import os

path = "bulk_file_renamer/"

# Check if the directory exists
if not os.path.exists(path):
    print("Error: Directory does not exist!")
    exit()

files = os.listdir(path)
new_name = input("New Name: ")

# Rename files while keeping their extensions
for idx, file in enumerate(files, start=1):
    old_path = os.path.join(path, file)
    
    # Extract file extension
    file_ext = os.path.splitext(file)[1]
    
    # Create new file name with extension
    new_path = os.path.join(path, f"{new_name} {idx}{file_ext}")
    
    # Rename file
    os.rename(old_path, new_path)

print(f"Renamed {len(files)} files successfully!")
