import os

from csf_StreetView import generateVideoFromKML

for root, dirs, files in os.walk("/var/www/staticfiles/kml/"):
    for fName in files:
        if fName.endswith(".kml"):
        	outFile = theVideoFileName.replace(".kml","").replace("kml_","video_") + ".mpeg"
        	if (not os.path.exists("/var/www/staticfiles/video/" + outfile)):
        		print (fname)
        		print ("/var/www/staticfiles/video/" + outfile)
        		kmlFile = os.path.join(fName)
            	#lines = open(kmlFile).read()
            	#generateVideoFromKML(lines,fName)



