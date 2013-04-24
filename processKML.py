import sys
import os
from cf_geo import distanceKM

sys.path.insert(0, '/pyxml')


kmlFile = os.path.join('exampleKML.kml')

lines = open(kmlFile).read()
content = lines.split('<LineString>')
allcoords = str(content[1])
coords = allcoords.split(' ')
i = 0

lastLLA = None
for txt in coords:
    if not txt.startswith('0') and not txt.startswith('<'):
        txt = txt.rstrip()
        llastr = txt.split(',')
        lla = [float(llastr[1]),float(llastr[0]),float(llastr[2])]
        dist = 0
        bearing = 0
        if lastLLA is not None:
            dist =  distanceKM([lastLLA[0],lastLLA[1]],[lla[0],lla[1]])
            bearing = bearing([lastLLA[0],lastLLA[1]],[lla[0],lla[1]])
        print "Dist: " + str(dist) + " Bearing: " + str(bearing) + " Lat: " + llastr[1] + " Lon: " + llastr[0] + " Alt: " + llastr[2]
        lastLLA = lla
    i+=1

 # doc = parser.parse(f)


