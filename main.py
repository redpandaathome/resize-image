# type "python3 main.py" in the ternimal to run 🏃🏻‍♀️🏃🏃‍♂️
from PIL import Image
import os
import random
directory = 'img'
newDirectory = 'resize'

def countFiles(directory):
   count = 0
   for root_dir, cur_dir, files in os.walk(directory):
      count += len(files)
   return count

def makeShuffledNames():
   fileNum = countFiles(directory)
   fileNameArr = [i for i in range(1, fileNum+1)]
   random.shuffle(fileNameArr)
   return fileNameArr

newNames = makeShuffledNames()
print(newNames)

def changeImgSize(oldPath, newPath):
   # Width base
   # basewidth = 464
   # img = Image.open(oldPath)
   # wpercent = (basewidth / float(img.size[0]))
   # hsize = int((float(img.size[1]) * float(wpercent)))
   # img = img.resize((basewidth, hsize), Image.ANTIALIAS)
   
   # Height base
   baseheight=550
   img = Image.open(oldPath)
   hpercent = (baseheight / float(img.size[1]))
   wsize = int((float(img.size[0]) * float(hpercent)))
   img = img.resize((wsize, baseheight), Image.ANTIALIAS)

   img.save(newPath, quality=90)


for i, filename in enumerate(os.listdir(directory)):
   f=os.path.join(directory, filename)
   if os.path.isfile(f):
      oldPath = f
      extension = os.path.splitext(filename)[1]
      if extension=='.gif':
         continue
      
      # A.JUST RESIZING
      newPath = os.path.join(newDirectory, filename)

      # B.RESIZING + FILE ORDER SHUFFLE
      # newPath = os.path.join(newDirectory, str(newNames[i])+extension)

      changeImgSize(oldPath, newPath)

