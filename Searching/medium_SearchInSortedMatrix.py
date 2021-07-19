def searchInSortedMatrix(matrix, target):
	for k in range(len(matrix)):
		for u in range(len(matrix[k])):
			if matrix[k][u] == target:
				return [k,u]
    return [-1,-1]
