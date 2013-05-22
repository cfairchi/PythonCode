#!/usr/bin/python
# _*_ coding: utf-8 _*_


import os
import Image


for root, dirs, files in os.walk("."):
    for fName in files:
        if fName.endswith(".png"):
		im = Image.open(fName)
		if im.mode != "RGB":
			im = im.convert("RGB")
		newName = fName.replace(".png",".jpg")
		print("replacing " + fName + " with " + newName)
		im.save(newName,"JPEG")
		


