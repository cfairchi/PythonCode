import sys
import os
from cf_geo import distanceKM
from cf_geo import bearing

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
        lat = float(llastr[1])
        lon = float(llastr[0])
        alt = float(llastr[2])
        lla = [round(lat,6),round(lon,6),round(alt,6)]
        dist = 0
        heading = 0
        if lastLLA is not None:
            dist =  round(distanceKM([lastLLA[0],lastLLA[1]],[lla[0],lla[1]]),2)
            heading = round(bearing([lastLLA[0],lastLLA[1]],[lla[0],lla[1]]),2)
        
        location = "&Location=" + str(lla[0]) + "," + str(lla[1])
        head = "&heading=" + str(heading)
        
        print "http://maps.googleapis.com/maps/api/streetview?size=300x200" + location + head + "&sensor=false"
        #print "Dist: " + str(dist) + " Bearing: " + str(heading) + " Location=" + llastr[1] + "," + llastr[0] + " Alt: " + llastr[2]
        lastLLA = lla
    i+=1

 # doc = parser.parse(f)


