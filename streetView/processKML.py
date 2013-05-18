import os

from csf_StreetView import generateVideoFromKML

requestCount = 0

for root, dirs, files in os.walk("/var/www/staticfiles/kml/"):
    for fName in files:
        if fName.endswith(".kml"):
        	outFile = fName.replace(".kml","").replace("kml_","video_") + ".avi"
                checkFile = "/var/www/staticfiles/video/" + outFile
		
		print ("Checking for " + checkFile)
        	if (not os.path.exists(checkFile)):
			if requestCount > 20000:
				print ("Aborting RequestCount=" + requestCount)
				break
			print("Processing " + outFile)
        		kmlFile = os.path.join(fName)
        		kmlFile = "/var/www/staticfiles/kml/" + kmlFile
        		#print (kmlFile)
			#print ("/var/www/staticfiles/video/" + outFile)
            		lines = open(kmlFile).read()
            		requestCount += generateVideoFromKML(lines,outFile)



