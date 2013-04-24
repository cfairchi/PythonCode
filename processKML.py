import sys
import os
from lxml import etree, objectify

sys.path.insert(0, '/pyxml')


kmlFile = os.path.join('exampleKML.kml')
with open(kmlFile) as f:
    print f.readlines()
 # doc = parser.parse(f)


