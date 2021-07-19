def tournamentWinner(competitions, results):
	i = []
	for k in range(len(competitions)):
		if results[k] == 0:
			i.append(competitions[k][1])
		elif results[k] == 1:
			i.append(competitions[k][0])
	x = []
	j = list(dict.fromkeys(i))
	for k in j:
		x.append(i.count(k))
	y = max(x)
	return j[x.index(y)]
