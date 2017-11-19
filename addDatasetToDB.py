import os
import utils
import sys
import sqlInterface as sql

if len(sys.argv) > 0:
	root = sys.argv[0]

root = '/Users/adel/Desktop/DatasetAudioFiles/'
file_path = ''
for folder in os.listdir(root):
	file_path = root + folder + '/'
	if os.path.isdir(file_path):
		for file in os.listdir(file_path):
			if os.path.isfile( file_path+file ) and file != '.DS_Store':
				row = utils.extractRow( file_path+file )
				sql.insertFromDic(row)
				print file_path+file
