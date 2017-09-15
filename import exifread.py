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
files = ["Samples/GalaxyS5.m4a"]
with exiftool.ExifTool() as et:
    allMetadata = et.get_metadata_batch(files)
    #print metadata
for metadata in allMetadata:
	#FORMATO QUERY MYSQL: INSERT INTO myDb.myTable('','') VALUES ('', '')
	queryHead, queryValues = "INSERT INTO pela.users(", ") VALUES ("
	firstTurn = 1
 	for key in metadata:
 		friendlyKey = key.split(":")[-1]
 		data = str(metadata[key])
 		if firstTurn:
	 		queryHead += friendlyKey 
	 		queryValues += data
	 		firstTurn = 0
	 	else:
	 		queryHead += "," + friendlyKey 
	 		queryValues += "," + data

 	
 	query = queryHead + queryValues + ")"
 	#print query
 	query = "ALTER TABLE pela.users ADD COLUMN sa VARCHAR(255)"
 	sql.runQuery(query)
 		#print friendlyKey+": "+str(metadata[key])
	print '________________________________'

    #print("{:20.20} {:20.20}".format(d["SourceFile"]))


