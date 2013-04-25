import os

from cf_StreetView import generateVideoFromKML

kmlFile = os.path.join('exampleKML.kml')
lines = open(kmlFile).read()
generateVideoFromKML(lines,"testVideoSV")

