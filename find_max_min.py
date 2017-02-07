def find_max_min(n):

	if len(set(n)) == 1:
		return list(set(n))
	else:
		l = len(n)
		n_sorted = sorted(n)

		minVal = n_sorted[0]
		maxVal = n_sorted[len(n)-1]

		return [minVal, maxVal]