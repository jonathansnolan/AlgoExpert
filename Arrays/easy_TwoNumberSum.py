def twoNumberSum(array, targetSum):
	for k in range(len(array)):
		for u in range(k+1,len(array)):
			if array[k] + array[u] == targetSum:
				return [array[k], array[u]]
	return []
