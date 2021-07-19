def runLengthEncoding(string):
	count = 1
	prev = "test"
	i = ""
	for k in string:
		if k == prev:
			count += 1
		else:
			if prev != "test" and count != 0:
				i += str(count) + prev
				prev = k
				count = 1
			else:
				prev = k
				count = 1
		if count == 9:
			i += str(count) + prev
			count = 0
	if i == "":
		i += str(count) + prev
	if len(i) > 1:
		if i[-1] != prev:
			i += str(count) + prev
		if i[-1] == prev and int(i[-2]) != count:
			i += str(count) + prev
	return i
