blackList = []
ignoredList = []

# with open( 'webapp/helpFiles/tagsBlackList.txt' ) as file:
# 	blackList = file.read().split("\n")
	
# with open( 'webapp/helpFiles/tagsIgnoredList.txt' ) as file:
# 	ignoredList = file.read().split("\n")

def distanceBetweenDictionaries(query, gallery):
	distance = 0
	for key in query:

		multiplier = 1
		if key not in blackList and (key in query) and (key in gallery):
			if key in ignoredList:
				multiplier = 80
			distance += distaceBetweenPair(query[key], gallery[key], key)*multiplier
	return distance

def distaceBetweenPair(p, q, key):
	distance = 0
	if str(p) != str(q):
		distance += 1	
	return distance
