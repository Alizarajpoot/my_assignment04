import os

path = "bulk_file_renamer/"

# Ensure the directory exists
if not os.path.exists(path):
    print("Error: Directory does not exist!")
    exit()

files = os.listdir(path)
print("Files in directory:", files)  # Debugging step

to_be_replaced = input("String to be replaced: ")
replacement = input("Replacement: ")

for file in files:
    if to_be_replaced in file:  # Check if "my" exists in filename
        old_path = os.path.join(path, file)
        new_filename = file.replace(to_be_replaced, replacement)
        new_path = os.path.join(path, new_filename)
        
        print(f"Renaming: {file} → {new_filename}")  # Debugging step
        
        os.rename(old_path, new_path)

print("Files renamed successfully!")
