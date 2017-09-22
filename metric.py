blacklist = {
			 'groundtruth', 
			 'SourceFile', 
			 'FileName', 
			 'id', 
			 'TrackModifyDate', 
			 'FileAccessDate', 
			 'FileModifyDate'
			}
whitelist = {
			 'Encoder'
			}

def distanceBetweenDictionaries(query, gallery):
	distance = 0
	for key in query:

		multiplier = 1
		if key in whitelist:
				multiplier = 10
		if key not in blacklist:
			distance += distaceBetweenPair(query[key], gallery[key])*multiplier
	return distance

def distaceBetweenPair(p, q):
	distance = 0
	if str(p) != str(q):
		distance += 1	
	return distance
