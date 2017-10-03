import sqlInterface as sql
import utils 
import json



deviceModel = 'GalaxyS4.m4a'
file = ["Samples/"+deviceModel]					
row = utils.extractRow(file, deviceModel)
sql.insertFromDic(row)
	

