import os

# Liệt kê các tệp và thư mục trong thư mục hiện tại
current_directory = os.getcwd()
files_and_folders = os.listdir(current_directory)

print("Current directory:", current_directory)
print("Files and folders:", files_and_folders)
        