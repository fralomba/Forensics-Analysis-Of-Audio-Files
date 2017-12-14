import pymysql

database = 'forensicsAnalysis'
user = 'root'
pw = 'root'
host = 'localhost'
port = 8889

#Insert rows in the database from a dictionari... basically create a string in the SQL Query format
def insertFromDic(dictionary):
    queryHead, queryValues = "INSERT INTO `dataset`(`id`", ") VALUES (NULL"
    for key in dictionary:    
        data = str(dictionary[key])
        #Haven't seen this key yet?!
        updateTables(key)
        #If it's not a duplicated field (no, if a key it's of EX that it's different by a MI key)
        if not(key in queryHead):
            queryHead += ",`" + key.replace("`", '"') + "`"
            queryValues += ",'" + data.replace("'", '"') + "'"

    query = queryHead + queryValues + ")"

    runQuery(query)

#this function get a Filed as parameter and, if it's a never seen Metadata, tables are updated to contain it.
def updateTables(field):
    #same routine... make a great query!
    query = "SELECT COUNT(Name) as 'occurrencies' FROM knownMetadata WHERE Name = '"+field.replace(' ','')+"'"
    
    result = runQuery(query)
    #if there is not...
    if result['occurrencies'] == 0:
        #add the metadata to the kowledge
        query = "INSERT INTO `knownMetadata` (`id`, `name`) VALUES (NULL, '"+field+"')"
        runQuery(query)
        #and add a column on the dataset table
        query = "ALTER TABLE `dataset` ADD `"+field+"`  VARCHAR(255) NULL DEFAULT NULL AFTER `id`;"
        runQuery(query)

#This function get a string and try to execue that on sql server. See pymysql documentation.

def runQuery(query):
    connection = pymysql.connect(host=host,user=user,password=pw,db=database,charset='utf8mb4',port=port,cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
        connection.commit()
    finally:
        connection.close()
    return result
#
def simplyfieDictionary(dictionary):
    newDict = {}
    for key in dictionary:
        friendlyKey = key.split(":")[-1]
        newDict[friendlyKey] = str(dictionary[key])
    return newDict



