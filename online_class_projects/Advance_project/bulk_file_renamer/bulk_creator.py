import os

# Define the directory
path = "bulk_file_renamer/"

# Ensure the directory exists
os.makedirs(path, exist_ok=True)

# Get the number of files
num_files = int(input("Enter the number of files: "))

# Create the files
for i in range(num_files):
    with open(f"{path}File_{i}.txt", "a") as file:  
        file.write(f"This is File_{i}\n")

print(f"{num_files} files created successfully in '{path}'.")
