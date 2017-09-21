#http://pymysql.readthedocs.io/en/latest/user/examples.html
import sqlConnection as sql
import exiftool
# with exiftool.ExifTool() as et:
# 	print path+file
# 	metadata = et.get_metadata_batch('/User/adel/Desktop/Samples/GalaxyS5.m4a')
deviceModel = 'macOsQuickTimeRecord.m4a'
files = ["Samples/"+deviceModel]
#files = ["Samples/GalaxyS5.m4a"]

with exiftool.ExifTool() as et:
    allMetadatas = et.get_metadata_batch(files)
    #print metadata
for metadata in allMetadatas:
	#FORMATO QUERY MYSQL: INSERT INTO myDb.myTable('','') VALUES ('', '')
	metadata['groundtruth'] = deviceModel.split('.')[0]
	# posso aggiungere cosa cazzo voglio 
	#sql.insertFromDic(metadata)
	print metadata