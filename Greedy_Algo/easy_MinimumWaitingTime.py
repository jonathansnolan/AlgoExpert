def minimumWaitingTime(queries):
	x = queries.sort()
	i = 0
	for k in range(len(queries)):
		i += sum(queries[:k])
	return i
