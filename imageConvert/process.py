#!/usr/bin/python
# _*_ coding: utf-8 _*_


import os
import Image

#basewidth = new width of image, example 300
def resizeImage(path, basewidth):
   import PIL
   from PIL import Image

   img = Image.open(path)
   wpercent = (basewidth/float(img.size[0]))
   hsize = int((float(img.size[1])*float(wpercent)))
   img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
   path = path.replace(".jpg","_300.jpg")
   img.save(path)
   print("Resized: " + path)
   
def convert(fName):
	if fName.endswith(".png"):
		im = Image.open(fName)
		if im.mode != "RGB":
			im = im.convert("RGB")
			newName = fName.replace(".png",".jpg")
			print("replacing " + fName + " with " + newName)
			im.save(newName,"JPEG")
		
for root, dirs, files in os.walk("."):
    for fName in files:
        if fName.endswith(".jpg"):
		resizeImage(path, 300)
		


