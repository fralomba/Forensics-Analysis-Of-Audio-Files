
import sys
import utils 

def perpareToJSON(dic):
	string = '[\n'
	
	for key in dic:
		string += "{ 'label':'" + str(key).replace("'",'"') + "', 'value':'" + str(dic[key]).replace("'",'"') + "'},\n"
	return string+"]"

if len(sys.argv) > 1:
	file = sys.argv[1]
else:
	file = "/Users/adel/Desktop/FAOAF/Samples/iphone7.m4a"

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
		
