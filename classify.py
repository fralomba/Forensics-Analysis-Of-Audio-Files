import sqlInterface as sql
import metric
import sys
import utils 

def perpareToJSON(dic):
	string = '['
	for key in dic:
		string += "{ 'label':' " + str(key) + "', 'value': " + str(dic[key]) + "},\n"
	return string+"]"

if len(sys.argv) > 1:
	file = sys.argv[1]
else:
	print "not enought arguments"

matchResult = {}

totRows = sql.runQuery("SELECT max(id) as 'tot' FROM dataset ")['tot']

queryElement = utils.extractRow(file)

for i in range(1, totRows+1):
	galleryElement = sql.runQuery("SELECT * FROM dataset WHERE id="+str(i))
	if galleryElement:
		distance = metric.distanceBetweenDictionaries(queryElement, galleryElement)
		matchResult[galleryElement['groundtruth']] = 10000000/distance

print perpareToJSON(matchResult)