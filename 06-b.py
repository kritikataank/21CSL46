import os
import sys
import pathlib
import zipfile

dirname = input("Enter Directory name that you want to back up: ")
if not os.path.isdir(dirname):
    print("Directory ", dirname, " doesn't exist.")
    sys.exit(0)

curdirectory = pathlib.Path(dirname)

with zipfile.ZipFile("myZip.zip", mode="w")as archive:
    for file_path in curdirectory.rglob("*"):
        archive.write(file_path, arcname=file_path.relative_to(curdirectory))

if os.path.isfile("myZip.zip"):
    print("Archive myZip.zip created successfully")
else:
    print("Error creating zip archive.")

