# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

import os

# Specify the path to the directory
directory_path = "/"

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print the contents of the directory
print(contents)

print("Contents of the directory:")
for item in contents:
    print(item)
