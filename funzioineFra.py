dato1 = {}
dato1['nome'] = 'hajy'
dato1['peso'] = '678'
dato1['sesso'] = '1'
dato1['forza'] = 'tanta'
dato1['stamina'] = 'molto poca'

dato2 = {}
dato2['nome'] = 'mine'
dato2['peso'] = '87kg'
dato2['sesso'] = 'M'
dato2['forza'] = 'media'
dato2['stamina'] = 'poca'

def distanceBetweenDictionaries(query, gallery):
	distance = 0
	for key in query:
		distance += distaceBetweenPair(query[key], gallery[key])
	return distance

def distaceBetweenPair(p, q):
	distance = 0
	#TODO pela fai
	return distance


distanceBetweenDictionaries(dato2, dato1)