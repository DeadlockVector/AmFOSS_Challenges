import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



card = Image.new('RGBA', (360, 288), 'white')
flower = Image.open('/home/isocyanate/flower.png')
card.paste(flower, (10, 40), flower)
cut_guide = Image.new('RGBA', (360, 288), 'black')
cut_guide.paste(card, (2, 2))

#TODO: fonts?
#TODO: save in folder along with guestname
#cut_guide.save(f'{name}-invite.png')


