dato1 = {}
dato1['nome'] = 'hajy'
dato1['peso'] = '678'
dato1['sesso'] = '1'
dato1['forza'] = 'tanta'
dato1['stamina'] = 'molto poca'

dato2 = {}
dato2['nome'] = 'mine'
dato2['peso'] = '87kg'
dato2['sesso'] = '1'
dato2['forza'] = 'media'
dato2['stamina'] = 'poca'

def distanceBetweenDictionaries(query, gallery):
	distance = 0
	for key in query:
		distance += distaceBetweenPair(query[key], gallery[key])

	print distance	
	return distance

def distaceBetweenPair(p, q):
	distance = 0
	
	if p != q:
		distance = 1

	return distance

distanceBetweenDictionaries(dato1, dato2)