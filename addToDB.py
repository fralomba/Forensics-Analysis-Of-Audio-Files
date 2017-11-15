import sqlInterface as sql
import utils 
import json

deviceModel = 'huaweiNovaPlus.amr'

file = "Samples/"+deviceModel					
row = utils.extractRow(file)
sql.insertFromDic(row)
	

