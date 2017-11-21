#http://pymysql.readthedocs.io/en/latest/user/examples.html
import sys
import utils 

def perpareToJSON(dic1, dic2, blackList, ignoredList):
	string = '[\n'
	
	for key in dic1:
		if key not in ignoredList:
			if key in dic2:
				string += "{ 'label':'" + str(key).replace("'",'"') + "', 'alert':'" + str((key in blackList) and (dic1[key] != dic2[key])) + "', 'value1':'" + str(dic1[key]).replace("'",'"') + "', 'value2':'" + str(dic2[key]).replace("'",'"') + "'},\n"
			else:
				string += "{ 'label':'" + str(key).replace("'",'"') + "', 'alert':'" + str(key in blackList) + "', 'value1':'" + str(dic1[key]).replace("'",'"') + "', 'value2':' ABSENT'},\n"

	for key in dic2:
		if key not in ignoredList:
			if key not in dic1 :
				string += "{ 'label':'" + str(key).replace("'",'"') + "', 'alert':'" + str(key in blackList) + "', 'value1':'ABSENT', 'value2':'" + str(dic2[key]).replace("'",'"') + "'},\n"
	return string+"]"
##_______________________________________________script starts here
#read input from command line
if len(sys.argv) > 1 and len(sys.argv) < 4:
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	blackList = []
	ignoredList = []
elif len(sys.argv) > 3:
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	with open( sys.argv[3] ) as file:
		blackList = file.read().split("\n")
	with open( sys.argv[4] ) as file:
		ignoredList = file.read().split("\n")
else:
	print "not enought arguments"

matchResult = {}

#e
queryElement = utils.extractRow(file1)
galleryElement = utils.extractRow(file2)

qResult = {}
for qKey in queryElement:
	if (qKey not in galleryElement) or (galleryElement[qKey] != queryElement[qKey]):
		qResult[qKey] = queryElement[qKey]

gResult = {}
for gKey in galleryElement:
	if (gKey not in queryElement) or (galleryElement[gKey] != queryElement[gKey]):
		gResult[gKey] = galleryElement[gKey]

#add lenght informations
gResult['LUNGHEZZA'] = len(galleryElement)
qResult['LUNGHEZZA'] = len(queryElement)

print ("var data = " + perpareToJSON(qResult, gResult, blackList, ignoredList) + ";")
		
