#!/usr/bin/python
# _*_ coding: utf-8 _*_


import os
import Image


for root, dirs, files in os.walk("~/git-repos/PythonCode/imageConvert/"):
    for fName in files:
	print fName
        if fName.endswith(".gif"):
		print fName


