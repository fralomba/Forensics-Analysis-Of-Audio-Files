#http://pymysql.readthedocs.io/en/latest/user/examples.html
import sqlConnection as sql
import exiftool


#help(exiftool)

path = "Samples/"
file = "GalaxyS5.m4a"

# with exiftool.ExifTool() as et:
# 	print path+file
# 	metadata = et.get_metadata_batch('/User/adel/Desktop/Samples/GalaxyS5.m4a')

files = ["Samples/GalaxyS5.m4a", "Samples/andre.mp3"]
#files = ["Samples/GalaxyS5.m4a"]

with exiftool.ExifTool() as et:
    allMetadatas = et.get_metadata_batch(files)
    #print metadata
for metadata in allMetadatas:
	#FORMATO QUERY MYSQL: INSERT INTO myDb.myTable('','') VALUES ('', '')
	
	sql.insertFromDic(metadata)