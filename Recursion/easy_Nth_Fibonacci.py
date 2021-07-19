def getNthFib(n):
	i = [0,1]
	count = 1
	for k in range(n):
		i.append(i[count]+i[count-1])
		count += 1
	return i[n-1]
