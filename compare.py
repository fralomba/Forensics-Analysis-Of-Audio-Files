#http://pymysql.readthedocs.io/en/latest/user/examples.html
import sqlInterface as sql
import exiftool
import metric
import numpy as np
import operator
# with exiftool.ExifTool() as et:
# 	print path+file
# 	metadata = et.get_metadata_batch('/User/adel/Desktop/Samples/GalaxyS5.m4a')


filename = 'GalaxyS5-audacity.m4a'
file = ["Samples/"+filename]

matchResult = {}

with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(file)[0]

totRows = sql.runQuery("SELECT max(id) as 'tot' FROM dataset ")['tot']
#    queryElement = sql.runQuery("SELECT * FROM dataset WHERE id="+str(totRows))
queryElement = sql.simplyfieDictionary(metadata)
for i in range(1, totRows+1):
	galleryElement = sql.runQuery("SELECT * FROM dataset WHERE id="+str(i))
	if galleryElement:
		distance = metric.distanceBetweenDictionaries(queryElement, galleryElement)
		matchResult[galleryElement['groundtruth']] = distance

sortedMatchResult = sorted(matchResult.items(), key=operator.itemgetter(1))
print "i migiori 5 risultati, in ordine, sono: \n"
print sortedMatchResult[0:5]


