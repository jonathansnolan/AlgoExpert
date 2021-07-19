def fourNumberSum(array, targetSum):
	i = []
	for k in range(0, len(array)-3):
		for u in range(k+1,len(array)-2):
			for z in range(u+1, len(array)-1):
				for w in range(z+1, len(array)):
					if array[k] + array[u] + array[z] + array[w] == targetSum:
						i.append([array[k], array[u], array[z], array[w]])
	return i
