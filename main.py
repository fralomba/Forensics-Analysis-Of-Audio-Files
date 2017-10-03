import sqlInterface as sql
import utils 
import json

<<<<<<< HEAD
deviceModel = 'iPhone6s.m4a'
=======


<<<<<<< HEAD
deviceModel = 'GalaxyS4.m4a'
>>>>>>> 5533a7b779510cc816b8dacff2c3722a8696ff21
=======
deviceModel = 'iphone6-audacity.m4a'
>>>>>>> eb3a749cc2a6268844b74ed3f7f5b9e92827e9f3
file = ["Samples/"+deviceModel]					
row = utils.extractRow(file, deviceModel)
sql.insertFromDic(row)
	

