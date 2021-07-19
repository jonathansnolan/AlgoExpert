def generateDocument(characters, document):
	x = characters
	y = document
	for k in y:
		if y.count(k) > x.count(k):
			return False
	return True
