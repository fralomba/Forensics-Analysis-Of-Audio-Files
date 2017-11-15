import os
import utils
import sqlInterface as sql

root = '/Users/adel/Desktop/datasetAudioFiles/'
file_path = ''
for folder in os.listdir(root):
	file_path = root + folder + '/'
	if os.path.isdir(file_path):
		for file in os.listdir(file_path):
			print file_path+file
			if os.path.isfile( file_path+file ) and file != '.DS_Store':
				row = utils.extractRow( file_path+file )
				sql.insertFromDic(row)