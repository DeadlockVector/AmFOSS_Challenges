import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('/home'):

    #number of files which aren't photos
    photos = 0
    non_photos = 0

    for filename in filenames:
        if not (filename.lower().endswith('jpg')) or (filename.lower().endswith('png')):
            non_photos += 1
            
        try:
            im = Image.open(os.path.join(foldername, filename))
        except OSError:
            continue
        
        w, h = im.size

        if w>500 and h>500:
            photos += 1
        else:
            non_photos += 1

    if photos>non_photos:
        print(os.path.abspath(foldername))