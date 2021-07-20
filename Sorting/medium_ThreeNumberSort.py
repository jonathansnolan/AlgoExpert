def threeNumberSort(array, order):
	for k in order:
		swap = "yes"
		while swap == "yes":
			swap = "no"
			for u in range(1,len(array)):
				if array[u] != k and array[u-1] == k:
					array[u], array[u-1] = array[u-1], array[u]
					swap = "yes"
	return array
