def prime_numbers(n):

	if not isinstance(n, int):
		raise ValueError("The provided input is not an integer.")

	result = []

	if n == 0 or n == 1:
		print (result)
	else:		
		for j in range(1,n+1):
			div = []

			for x in range(1,n+1):
				if j%x == 0:
					div.append(x)

			if (len(div) == 2):
				result.append(j)

		print (result)