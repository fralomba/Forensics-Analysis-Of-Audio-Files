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
		string += "{ 'label':' " + str(key) + "', 'value': " + str(dic[key]) + "},"
	return string+"]"

if len(sys.argv) > 2:
	file1 = [sys.argv[1]]
	file2 = [sys.argv[2]]
else:
	file1 = ["/Users/francesco/Desktop/Forensics-Analysis-Of-Audio-Files/Samples/iphone7.m4a"]
	file2 = ["/Users/francesco/Desktop/Forensics-Analysis-Of-Audio-Files/Samples/iphone6s.m4a"]

matchResult = {}

# with exiftool.ExifTool() as et:
#     metadata = et.get_metadata_batch(file)[0]

queryElement = json.dumps(utils.extractRow(file1, 'NONE'))
galleryElement = json.dumps(utils.extractRow(file1, 'NONE'))

print queryElement
print galleryElement
