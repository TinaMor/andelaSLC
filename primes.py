def prime_numbers(n):

	# First we check in the input is of the type integer
	if not isinstance(n, int):
		raise ValueError("The provided input is not an integer.")

	result = []

	# Retunrs an empty list for n = 0 or 1
	if n == 0 or n == 1:
		print (result)
	else:		
		for j in range(1,n+1):
			div = []

			for x in range(1,n+1):
				if j%x == 0:
					div.append(x)

			if (len(div) == 2): #Since a prime number is only divisible by one and itself, the list of divisors has the length of 2
				result.append(j)

		print (result)