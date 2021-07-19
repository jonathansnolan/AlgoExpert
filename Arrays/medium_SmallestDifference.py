def smallestDifference(arrayOne, arrayTwo):
    small = min(arrayOne) + max(arrayTwo)
	i = []
	for k in arrayOne:
		for u in arrayTwo:
			j = u - k
			if j < 0:
				j *= -1
			if small > j:
				small = j
				i = [k,u]
	return i
