def subarraySort(array):
	i = ""
	j = ""
	for k in range(len(array)-1):
		if array[k] > min(array[k+1:]):
			i = k
			break
	x = array[::-1]
	for u in range(0,len(x)-1):
		if x[u] < max(x[u+1:]):
			j = len(x) - u -1
			break
	if i == "" and j == "":
		return [-1,-1]
	else:
		return[i,j]
