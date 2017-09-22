#http://pymysql.readthedocs.io/en/latest/user/examples.html
import sqlInterface as sql
import exiftool
import metric
import numpy as np
import operator
# with exiftool.ExifTool() as et:
# 	print path+file
# 	metadata = et.get_metadata_batch('/User/adel/Desktop/Samples/GalaxyS5.m4a')

<<<<<<< HEAD
filename = 'GalaxyS4.m4a'
=======
filename = 'iphone7.m4a'
>>>>>>> origin/master
file = ["Samples/"+filename]
#files = ["Samples/GalaxyS5.m4a"]

devices = []
distances = []

matchResult = {}

with exiftool.ExifTool() as et:
<<<<<<< HEAD
    metadata = et.get_metadata_batch(file)[0]
    print sql.simplyfieDictionary(metadata)
 #    sql.insertFromDic(metadata)

    totRows = sql.runQuery("SELECT max(id) as 'tot' FROM dataset ")['tot']
 #    queryElement = sql.runQuery("SELECT * FROM dataset WHERE id="+str(totRows))
    queryElement = sql.simplyfieDictionary(metadata)
    for i in range(1, totRows+1):
    	galleryElement = sql.runQuery("SELECT * FROM dataset WHERE id="+str(i))
    	if galleryElement:
    		distance = metric.distanceBetweenDictionaries(queryElement, galleryElement)
    		print str(galleryElement['groundtruth']) + '  ' + str(distance)
	# sql.runQuery("DELETE FROM dataset WHERE id = "+str(totRows))
=======
	metadata = et.get_metadata_batch(file)[0]
	sql.insertFromDic(metadata)

	totRows = sql.runQuery("SELECT max(id) as 'tot' FROM dataset ")['tot']
	queryElement = sql.runQuery("SELECT * FROM dataset WHERE id="+str(totRows))
	for i in range(1, totRows):
		galleryElement = sql.runQuery("SELECT * FROM dataset WHERE id="+str(i))
		if galleryElement:
			distance = metric.distanceBetweenDictionaries(galleryElement, queryElement)
			devices.append(str(galleryElement['groundtruth']))
			distances.append(str(distance))

	sql.runQuery("DELETE FROM dataset WHERE id = "+str(totRows))

	for i in range(len(devices)):
		matchResult[devices[i]] = distances[i]

	print matchResult
	print"\n"

	sortedMatchResult = sorted(matchResult.items(), key=operator.itemgetter(1))
	print "i migiori 5 risultati, in ordine, sono: \n"
	print sortedMatchResult[0:5]


>>>>>>> origin/master
