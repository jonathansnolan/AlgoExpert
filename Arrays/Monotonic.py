def isMonotonic(array):
	if array == [] or len(array) == 1:
		return True

	x = sorted(array)
	if array == x or array == x[::-1]:
		return True
	return False
