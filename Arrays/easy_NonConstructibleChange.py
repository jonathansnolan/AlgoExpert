def nonConstructibleChange(coins):
	coins.sort()

	change = 0
	for k in coins:
		if k > change + 1 and change != 0:
			return change + 1
		change += k
	return change + 1


print(nonConstructibleChange([2,3,4,7,10]))
