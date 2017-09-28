#http://pymysql.readthedocs.io/en/latest/user/examples.html
import sqlInterface as sql
import operator
import metric
import sys
import utils 

if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	filename = 'iPhone6.m4a'

file = ["/Users/adel/Desktop/FAOAF/Samples/"+filename]
matchResult = {}

# with exiftool.ExifTool() as et:
#     metadata = et.get_metadata_batch(file)[0]
totRows = sql.runQuery("SELECT max(id) as 'tot' FROM dataset ")['tot']

queryElement = utils.extractRow(file, filename)

for i in range(1, totRows+1):
	galleryElement = sql.runQuery("SELECT * FROM dataset WHERE id="+str(i))
	if galleryElement:
		distance = metric.distanceBetweenDictionaries(queryElement, galleryElement)
		matchResult[galleryElement['groundtruth']] = distance


sortedMatchResult = sorted(matchResult.items(), key=operator.itemgetter(1))

print sortedMatchResult[0:5]


