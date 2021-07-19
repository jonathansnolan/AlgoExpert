def threeNumberSum(array, targetSum):
	i = []
	for k in range(len(array)-2):
		for u in range(k+1,len(array)-1):
			for z in range(u+1,len(array)):
				if array[k] + array[u] + array[z] == targetSum:
					i.append(sorted([array[k],array[u],array[z]]))
	return sorted(i)
