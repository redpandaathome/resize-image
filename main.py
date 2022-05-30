# type "python3 main.py" in the ternimal to run 🏃🏻‍♀️🏃🏃‍♂️
from PIL import Image
import os
directory = 'img'
newDirectory = 'resize'

def changeImgSize(oldPath, newPath):
   basewidth = 600
   img = Image.open(oldPath)
   wpercent = (basewidth / float(img.size[0]))
   hsize = int((float(img.size[1]) * float(wpercent)))
   img = img.resize((basewidth, hsize), Image.ANTIALIAS)
   img.save(newPath, quality=90)

for filename in os.listdir(directory):
   f=os.path.join(directory, filename)
   if os.path.isfile(f):
      oldPath = f
      newPath = os.path.join(newDirectory, filename)
      changeImgSize(oldPath, newPath)

