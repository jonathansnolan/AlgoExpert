def minimumCharactersForWords(words):
	i = {}
	for k in words:
		x = list(dict.fromkeys(k))
		for u in x:
			if u not in i:
				i[u] = k.count(u)
			elif u in i and k.count(u) > i[u]:
				i[u] = k.count(u)
    ans = []
	for k in i:
		if i[k] == 1:
			ans.append(k)
		else:
			for u in range(i[k]):
				ans.append(k)
	return ans
	
