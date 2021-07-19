def largestRange(array):
	if len(array) == 1:
		return [array[0],array[0]]
	array = sorted(array)
	array = list(dict.fromkeys(array))
	i = []
	j = []
	for k in range(len(array)-1):
		if (array[k]+1) == array[k+1]:
			if array[k] in j:
				j.append(array[k+1])
			else:
				j.append(array[k])
				j.append(array[k+1])
		else:
			if j != []:
				i.append(j)
			j = []
	if j not in i and j != []:
		i.append(j)
	x = sorted(i, key = len)
	x = x[-1]
	return [x[0],x[-1]]
