import shutil, os

directory = "/home/isocyanate/Desktop/OsWalk"
for folderName, subfolders, filenames in os.walk(directory):
    
    for subfolder in subfolders:
        subfolderPath = folderName+'/'+subfolder
        if os.path.getsize(subfolderPath) > 102400:
            #shutil.rmtree(subfolderPath)
            pass

    for filename in filenames:
        filepath = folderName+'/'+filename
        if os.path.getsize(filepath) > 102400:
            #os.unlink(filepath)
            pass

# TODO: Figure out a way to test the working