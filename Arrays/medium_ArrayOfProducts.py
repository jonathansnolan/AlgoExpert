def arrayOfProducts(array):
	i = []
	for k in range(len(array)):
		j = 1
		if k == 0:
			u = array[k+1:]
		elif k == len(array):
			u = array[:k]
		else:
			u = array[:k] + array[k+1:]

		for x in u:
			j *= x
		i.append(j)
	return i
