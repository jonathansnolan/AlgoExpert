def reverseWordsInString(string):
	if len(string) <= 1:
		return string

	x = ""
	w = ""
	i = []

	for k in string:
		if k != " ":
			x += k
			i.append(w)
			w = ""
		elif k == " " and x != "":
			i.append(x)
			x = ""
		if k == " ":
			w += " "
	if i[-1] != x:
		i.append(x)
	if w != "":
		i.append(w)

	i = i[::-1]
	j = ""
	for k in i:
		j += k
	return j
