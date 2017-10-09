#http://pymysql.readthedocs.io/en/latest/user/examples.html
import sqlInterface as sql
import operator
import metric
import sys
import utils 

def perpareToJSON(dic):
	string = '['
	for key in dic:
		string += "{ 'label':' " + str(key) + "', 'value': " + str(dic[key]) + "},"
	return string+"]"

if len(sys.argv) > 1:
	file = sys.argv[1]
else:
	filename = 'iphone6.m4a'
	file = "/Users/francesco/Desktop/Forensics-Analysis-Of-Audio-Files/Samples/"+filename

matchResult = {}
# with exiftool.ExifTool() as et:
#     metadata = et.get_metadata_batch(file)[0]
totRows = sql.runQuery("SELECT max(id) as 'tot' FROM dataset ")['tot']

queryElement = utils.extractRow(file, 'NONE')

for i in range(1, totRows+1):
	galleryElement = sql.runQuery("SELECT * FROM dataset WHERE id="+str(i))
	if galleryElement:
		distance = metric.distanceBetweenDictionaries(queryElement, galleryElement)
		matchResult[galleryElement['groundtruth']] = 10000000/distance

print perpareToJSON(matchResult)