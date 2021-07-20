def longestSubstringWithoutDuplication(string):
	if len(string) <= 1:
		return string
	long = ""
	for k in range(len(string)-1):
		i = [string[k]]
		for u in range(k+1,len(string)):
			if string[u] not in i:
				i.append(string[u])
			else:
				if len(long) < len(i):
					long = i
				break
		if len(long) < len(i):
			long = i
	j = ""
	for k in long:
		j += k
	return j
