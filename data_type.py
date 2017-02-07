def data_type(n):
	if isinstance(n, str):
		return (len(n))
	elif n == None:
		return 'no value'
	elif n == True or n == False:
		return n
	elif isinstance(n, int):
		if n < 100:
			return 'less than 100'
		elif n > 100:
			return 'more than 100'
		elif n == 100:
			return 'equal to 100'
	elif isinstance(n, list):
		if len(n) > 2:
			return n[2]
		else:
			return 'None'