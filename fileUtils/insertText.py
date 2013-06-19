import os

def insertText(directory, extension, text):
  for root, dirs, files in os.walk(directory):
    for fName in files:
        if fName.endswith(extension):
          os.rename( fName, fName+"~" )
          f = open(fName,"w+")
          f.write(text)
          lines = open(fName+"~").read()
          for line in lines:
            f.write(line)
          f.Close  


insertText(".", ".cs" ,"//*****************************************************************")
