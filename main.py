import sqlInterface as sql
import utils 
import json



deviceModel = 'iPhone6s.m4a'
file = ["Samples/"+deviceModel]					
row = utils.extractRow(file, deviceModel)
sql.insertFromDic(row)
	

