def firstNonRepeatingCharacter(string):
	for k in string:
		if string.count(k) == 1:
			return string.index(k)
	return -1
