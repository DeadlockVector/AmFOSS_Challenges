import shutil, os

#original directory
og_directory = "/home/isocyanate/Desktop/OsWalk"

#new organized directory
new_directory = "/home/isocyanate/Desktop/AmFOSS_Challenges/Chapter10/SelectiveSort/NewDirectory"

file_extension = input('Enter the file extension to be searched - ')
#testing with .txt now
#file_extension = '.txt'

#os.walk() to traverse through the whole file tree
for folderName, subfolders, filenames in os.walk(og_directory):
    for filename in filenames:
        if filename.endswith(file_extension):
            print('Copying', filename, 'in', folderName)
            shutil.copy(folderName+'/'+filename, new_directory)

