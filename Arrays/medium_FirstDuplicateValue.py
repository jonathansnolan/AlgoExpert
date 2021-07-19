def firstDuplicateValue(array):
	i = []
	for k in array:
		if k not in i:
			i.append(k)
		else:
			return k
	return -1
