import os

from csf_StreetView import generateVideoFromKML

for root, dirs, files in os.walk(os.getcwd()):
    for fName in files:
        if fName.endswith(".kml"):
            kmlFile = os.path.join(fName)
            lines = open(kmlFile).read()
            generateVideoFromKML(lines,fName)



