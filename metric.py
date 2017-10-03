blacklist = {
			 'ET:groundtruth', 
			 'ET:SourceFile', 
			 'ET:FileName', 
			 'ET:id', 
			 'ET:TrackModifyDate', 
			 'ET:FileAccessDate', 
			 'ET:FileModifyDate',
			 'ET:TrackModifyDate',
			 'ET:TrackCreateDate'
			}
whitelist = {
			 'ET:Encoder',
			 'ET:FileTypeExtension',
			 'ET:TimeScale',
			 'MI:other_frame_rate',
			 'ET:HandlerType'
			}

def distanceBetweenDictionaries(query, gallery):
	distance = 0
	for key in query:

		multiplier = 1
		if key not in blacklist and (key in query) and (key in gallery):
			if key in whitelist:
				multiplier = 80
			distance += distaceBetweenPair(query[key], gallery[key])*multiplier
	return distance

def distaceBetweenPair(p, q):
	distance = 0
	if str(p) != str(q):
		distance += 1	
	return distance
