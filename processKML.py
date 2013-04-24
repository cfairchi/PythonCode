from pykml import parser

kmlFile = path.join('exampleKML.kml')
with open(kmlFile) as f:
  doc = parser.parse(f)

print doc
