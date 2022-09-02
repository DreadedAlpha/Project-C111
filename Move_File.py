import os
import shutil
from turtle import ScrolledCanvas
from_dir = "C:\Users\Aarush Penmetsa\Downloads"
to_dir = "C:\Users\Aarush Penmetsa\Documents\Document_Files"
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)