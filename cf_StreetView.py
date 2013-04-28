import sys
import os
import urllib
import cv
import Image
import time

from cf_geo import distanceKM
from cf_geo import bearing

def generateVideoFromKML(thekml, theVideoFileName):
    content = thekml.split('<LineString>')
    allcoords = str(content[1])
    coords = allcoords.split(' ')
    i = 0
    fourcc = cv.CV_FOURCC('P','I','M','1')
    outFile = theVideoFileName + ".mpeg"
    w = cv.CreateVideoWriter(outFile, fourcc, 24,(400,300), is_color=1)

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
                heading = int(bearing([lastLLA[0],lastLLA[1]],[lla[0],lla[1]]))
            
            location = "&location=" + str(lla[0]) + ",%20" + str(lla[1])
            head = "&heading=" + str(heading)
            
            urlString = "http://maps.googleapis.com/maps/api/streetview?size=400x300" + location + "&fov=90" + head + "&pitch=10&sensor=false&key=AIzaSyBqftMUNYnTPUaNRoovD9AfCeHyye8H6lk"
            urllib.urlretrieve(urlString, "sv_" + str(i) +".jpg")
            statinfo = os.stat("sv_" + str(i) +".jpg")
            #print statinfo.st_size
            if (statinfo.st_size > 5000):
                #print urlString
                img = cv.LoadImage("sv_" + str(i) +".jpg")
                #im.save("sv_" + str(i) +".png")
                for x in range(0, 5):
                    cv.WriteFrame(w, img)

            os.remove("sv_" + str(i) +".jpg")
            lastLLA = lla
            #if i >50: break
            #time.sleep(1)
            print i
            i+=1
    print str(i) + " Images Processed"
    
        