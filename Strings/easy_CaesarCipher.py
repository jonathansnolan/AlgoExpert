def caesarCipherEncryptor(string, key):
	i = ""
	for k in string:
		x = ord(k)
		x += key
		while x > 122:
			x -= 26
		i += chr(x)
	return i
