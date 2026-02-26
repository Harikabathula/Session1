"""
Docstring for harika_module on shutil

organizing the files in folders/documents in system
"""
import os
import shutil


print("------ Files organizer--------")
# folders having files to organize
folder_path="E:/Algorithms" 

for file_name in os.listdir(folder_path):
    if "." in file_name:
        ext=file_name.split(".")[-1]
        ext_folder=os.path.join(folder_path,ext)

        if not os.path.exists(ext_folder):
            os.makedirs(ext_folder)

        shutil.move(
            os.path.join(folder_path,file_name),
            os.path.join(ext_folder,file_name)
        )



print("Files are Organized Successfully")