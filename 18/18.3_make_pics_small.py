'''
Diminishes the size of all .png files by half.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 18.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from PIL import Image
import os

for filename in os.listdir('pic'):
    if filename.endswith('.png'):
        im = Image.open(filename)
        x = im.size[0]
        y = int(im.size[1] / 2)
        small = im.resize((x, y))
        small.save('pic/small_'+filename)
