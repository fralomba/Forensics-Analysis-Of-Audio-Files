#http://pymysql.readthedocs.io/en/latest/user/examples.html
import sqlInterface as sql
import exiftool
import funzioineFra as metric
# with exiftool.ExifTool() as et:
# 	print path+file
# 	metadata = et.get_metadata_batch('/User/adel/Desktop/Samples/GalaxyS5.m4a')

filename = 'GalaxyS4.m4a'
file = ["Samples/"+filename]
#files = ["Samples/GalaxyS5.m4a"]

with exiftool.ExifTool() as et:
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
