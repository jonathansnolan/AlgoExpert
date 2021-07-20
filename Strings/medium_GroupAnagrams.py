def groupAnagrams(words):
	if len(words) == 0:
		return []

	i = []
	completed = []

	for k in range(len(words)-1):
		j = [words[k]]
		if words[k] in completed:
			continue

		for u in range(k+1, len(words)):
			if sorted(words[k]) == sorted(words[u]):
				j.append(words[u])
				completed.append(words[u])

		if len(j) > 1:
			i.append(j)
		elif words[k] not in completed:
			i.append([words[k]])

	if words[-1] not in completed:
		i.append([words[-1]])
	return i
