import sqlInterface as sql
import exiftool
from pymediainfo import MediaInfo
import json
# with exiftool.ExifTool() as et:
# 	print path+file
# 	metadata = et.get_metadata_batch('/User/adel/Desktop/Samples/GalaxyS5.m4a')
def cleanKey(key, prefix):
	return prefix + ":" + key.split(":")[-1]

#files = ["Samples/GalaxyS5.m4a"]
def extractRow(file, deviceModel):
	with exiftool.ExifTool() as et:
	    allMetadatas = et.get_metadata_batch([file])
	    #print metadata

	MI = MediaInfo.parse(file)
	mediaInfo = json.loads(MI.to_json())

	for metadata in allMetadatas:
		row = {}
		#FORMATO QUERY MYSQL: INSERT INTO myDb.myTable('','') VALUES ('', '')
		row['groundtruth'] = deviceModel.split('.')[0]
	#EXTRACT FROM EXIFTOOL
		for key in metadata:
			if metadata[key]:
				row[cleanKey(key,'ET')] = metadata[key]
			else:
				row[cleanKey(key,'ET')] = "PENE"

	#EXTRACT FROM MEDIA INFO
		for firstKey in mediaInfo:
			for secondKey in mediaInfo[firstKey]:
				for key in secondKey:
					row[cleanKey(key,'MI')] = secondKey[key]
		return row


