import os

root = '/Users/francesco/Desktop/SamplesBuoniFAOAF2/'
i = 0
for folder in os.listdir(root):
	if os.path.isdir(root + folder) and folder[0] != 'D' and folder[1] != '0':
		os.rename(root + folder, root + 'D00' + str(i) + '_' + folder)		#cambia nome alle cartelle
		i = i+1

i = 0
for folder in os.listdir(root):
	folderpath = root + folder + '/' 
	if os.path.isdir(folderpath):
		for file in os.listdir(folderpath):			#cambia nome ai file dentro le cartelle
			if os.path.isfile(folderpath + file) and file != '.DS_Store':
				suffix = file[-3:]
				os.rename(folderpath + file, folderpath + folder[5:] + '_sample' + str(i) + '.' + suffix)
				i = i+1
		i = 0