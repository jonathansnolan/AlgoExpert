def moveElementToEnd(array, toMove):
	i = []
	j = []
	for k in array:
		if k == toMove:
			j.append(k)
		else:
			i.append(k)
    return i + j
