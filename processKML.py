import os

from cf_StreetView import generateVideoFromKML

kmlFile = os.path.join('colorado-colorado-national-monument.kml')
lines = open(kmlFile).read()
generateVideoFromKML(lines,"colorado-colorado-national-monument")

