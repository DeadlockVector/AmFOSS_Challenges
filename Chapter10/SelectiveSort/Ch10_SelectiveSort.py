import shutil, os
from pathlib import Path

#to keep track of file extensions
list_fileExtensions = []

#original directory
og_directory = "/home/isocyanate/Desktop/OsWalk"

#new organized directory
new_directory = "/home/isocyanate/Desktop/AmFOSS_Challenges/Chapter10/SelectiveSort/NewDirectory"

#TODO: take input for file extension,
#testing with .txt now
file_extension = '.txt'
p = Path.home()
for folderName, subfolders, filenames in os.walk(og_directory):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        if filename.endswith(file_extension):
            #shutil.copy(p/filename, new_directory)
            print(new_directory)
        print('FILE INSIDE ' + folderName + ': '+ filename)
    print()

# TODO: Figure out a way to get file extensions with os.walk()
# TODO: check extension, if same copy
