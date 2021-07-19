def isValidSubsequence(array, sequence):
	i = []
	for k in array:
		if k in sequence:
			i.append(k)
			if i == sequence:
				return True
	return False
