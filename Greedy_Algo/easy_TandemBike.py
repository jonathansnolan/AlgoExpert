def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	
	i = []

	x = sorted(redShirtSpeeds)
	x = x[::-1]
	y = sorted(blueShirtSpeeds)
	if fastest == True:
		for k in range(len(x)):
			i.append(max(x[k],y[k]))
		return sum(i)
	else:
		x = x[::-1]
		for k in range(len(x)):
			i.append(max(x[k],y[k]))
		return sum(i)
