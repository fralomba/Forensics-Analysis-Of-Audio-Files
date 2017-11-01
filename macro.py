#http://pymysql.readthedocs.io/en/latest/user/examples.html
import sqlInterface as sql
import operator
import metric
import sys
import json
import utils 

def perpareToJSON(dic):
	string = '['
	
	for key in dic:
		string += "{ 'label':'" + str(key).replace("'",'"') + "', 'value':'" + str(dic[key]).replace("'",'"') + "'},"
	return string+"]"

if len(sys.argv) > 1:
	file = sys.argv[1]
else:
	file = "/Users/adel/Desktop/dataset FAOAF/d003_LG_Nexus5_7.0.1/Muto.wav"

matchResult = {}

# with exiftool.ExifTool() as et: 
#     metadata = et.get_metadata_batch(file)[0]

queryElement = utils.extractRow(file)

qResult = {}
for qKey in queryElement:
	qResult[qKey] = queryElement[qKey]

#add lenght informations
qResult['LUNGHEZZA'] = len(queryElement)

print "var data = " + perpareToJSON(qResult) + ";"
		
