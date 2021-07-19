def findThreeLargestNumbers(array):
	swap = "yes"
	while swap == "yes":
		swap = "no"
		for k in range(0, len(array)-1):
			if array[k] < array[k+1]:
				array[k], array[k+1] = array[k+1], array[k]
				swap = "yes"
	x = array[:3]
	return x[::-1]
