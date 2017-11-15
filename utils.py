import sqlInterface as sql
import exiftool
from pymediainfo import MediaInfo
import json
# with exiftool.ExifTool() as et:
# 	print path+file
# 	metadata = et.get_metadata_batch('/User/adel/Desktop/Samples/GalaxyS5.m4a')

#The keys comes as a concatenation of more strings, separated by ":"
def cleanKey(key, prefix):
	return prefix + ":" + key.split(":")[-1]

#This fuction extract informations from the file at the path "file_path"
def extractRow(file_path):
	# Initialize the tool
	with exiftool.ExifTool() as et:
	    allMetadatas = et.get_metadata_batch([file_path])
	    ETmetadata = allMetadatas[0]
	# Initialize the tool
	MI = MediaInfo.parse(file_path)
	mediaInfo = json.loads(MI.to_json())

		
	row = {}
	row['groundtruth'] = file_path.split('/')[-1]
#EXTRACT FROM EXIFTOOL
#____________________________________________________Extraction using exiftool: see documentation for routine
	for key in ETmetadata:
		if ETmetadata[key]:
			row[cleanKey(key,'ET')] = ETmetadata[key]
		else:
			row[cleanKey(key,'ET')] = "xxx"

#EXTRACT FROM MEDIA INFO
#____________________________________________________Extraction using MediaInfo: see documentation for routine
	for firstKey in mediaInfo:
		for secondKey in mediaInfo[firstKey]:
			for key in secondKey:
				row[cleanKey(key,'MI')] = secondKey[key]
	return row


