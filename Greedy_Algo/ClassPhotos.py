def classPhotos(redShirtHeights, blueShirtHeights):
	x = sorted(redShirtHeights)
	y = sorted(blueShirtHeights)
	if x[0] > y[0]:
		for k in range(len(x)):
			if x[k] <= y[k]:
				return False
		return True
	if x[0] < y[0]:
		for k in range(len(x)):
			if x[k] >= y[k]:
				return False
		return True
    # Write your code here.
    return False
