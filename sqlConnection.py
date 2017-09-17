import pymysql

def insertFromDic(dictionary):
    connection = pymysql.connect(host='127.0.0.1',user='root',password='root',db='pela',charset='utf8mb4',port=8889,cursorclass=pymysql.cursors.DictCursor)
    
    queryHead, queryValues = "INSERT INTO `dataset`(`id`", ") VALUES (NULL"
    for key in dictionary:
        
        friendlyKey = key.split(":")[-1]
        data = str(dictionary[key])
        
        updateTables(friendlyKey)

        queryHead += ",`" + friendlyKey.replace("`", '"') + "`"
        queryValues += ",'" + data.replace("'", '"') + "'"

    query = queryHead + queryValues + ")"
    print query
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
       connection.commit()
    finally:
        connection.close()

#this function get a Filed as parameter and, if it's a never seen Metadata, tables are updated to contain it.
def updateTables(field):
    connection = pymysql.connect(host='127.0.0.1',user='root',password='root',db='pela',charset='utf8mb4',port=8889,cursorclass=pymysql.cursors.DictCursor)
    #this query check if there is an occurrence of the field
    query = "SELECT COUNT(Name) as 'occurrencies' FROM knownMetadata WHERE Name = '"+field+"'"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            #if there is not...
            if result['occurrencies'] == 0:
                #add the metadata to the kowledge
                query = "INSERT INTO `knownMetadata` (`id`, `Name`) VALUES (NULL, '"+field+"')"
                cursor.execute(query)
                #and add a column on the dataset table
                query = "ALTER TABLE `dataset` ADD `"+field+"`  VARCHAR(255) NULL DEFAULT NULL AFTER `id`;"
                cursor.execute(query)
        connection.commit()
    finally:
        connection.close()












