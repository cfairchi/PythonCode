import sys
import os
import urllib
import cv
import Image
import time

lib_path = os.path.abspath('../pyUtils/')
sys.path.append(lib_path)

from csf_Geo import distanceKM
from csf_Geo import bearing
from GoogleAPIKey import getGoogleAPIKey

def generateVideoFromCoords(theCoords, theVideoFileName):
    i = 0
    requestCount = 0
    fourcc = cv.CV_FOURCC('X','V','I','D')
    outFile = theVideoFileName #theVideoFileName.replace(".kml","").replace("kml_","video_") + ".avi"
    w = cv.CreateVideoWriter(outFile, fourcc, 30,(300,200), is_color=1)

    lastLLA = None
    
    skip = 0
    for txt in theCoords:
        if not txt.startswith('0') and not txt.startswith('<') and not txt == "" and not skip==1:
            print(txt)
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
            
            urlString = "http://maps.googleapis.com/maps/api/streetview?size=300x300" + location + "&fov=90" + head + "&pitch=10&sensor=false" + getGoogleAPIKey()
            urllib.urlretrieve(urlString, "sv_" + str(i) +".jpg")
            requestCount += 1
            statinfo = os.stat("sv_" + str(i) +".jpg")
            if (statinfo.st_size > 5000):
                img = cv.LoadImage("sv_" + str(i) +".jpg")
                slip = 1
                for x in range(0, 4):
                    cv.WriteFrame(w, img)

            os.remove("sv_" + str(i) +".jpg")
            lastLLA = lla
            print i
            i+=1
        else:
            skip = 0
    print str(i) + " Images Processed"
    return requestCount
    
def generateVideoFromKML(thekml, theVideoFileName):
    requests = 0
    content = thekml.split('<coordinates>')
    allcoords = ""
    for i in range(1,len(content)):
    	#print (content[i].split("</coordinates>")[0])
    	allcoords = allcoords + content[i].split("</coordinates>")[0] + " "
    
    outFile = theVideoFileName#.replace(".kml","").replace("kml_","video_") + ".mpeg"
    coords = allcoords.split(' ')
    if (not os.path.exists(outFile)):
	requests = generateVideoFromCoords(coords,theVideoFileName)
    else:
        print("File already exists: " + theVideoFileName)
    
    return requests
    
        

