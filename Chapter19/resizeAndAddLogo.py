import os
from PIL import Image

SQUARE_FIT_SIZE = 300
#tested with sample image
LOGO_FILENAME = '/home/isocyanate/car.jpg'

logo_im = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_im.size

os.makedirs('/home/isocyanate/Desktop/AmFOSS_Challenges/Chapter19/withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('/home/isocyanate/Desktop/AmFOSS_Challenges/Chapter19/Images'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')
            or filename.lower().endswith('.gif') or filename.lower().endswith('bmp')) \
            or filename == LOGO_FILENAME:
        continue   # Skip non-image files and the logo itself.

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

    # Resize the image.
    print(f'Resizing {filename}...')
    im = im.resize((width, height))

    # Add the logo if the image size is large enough for it to look good.
    width, height = im.size
    if width < logo_width * 2 or height < logo_height * 2:
        print("Photo skipped, but added to directory")
    else:
        print('Adding logo to', filename)
        im.paste(logo_im, (width - logo_width, height - logo_height), logo_im)
        
    im.save(os.path.join('/home/isocyanate/Desktop/AmFOSS_Challenges/Chapter19/withLogo', filename))