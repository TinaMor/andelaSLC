def find_missing(list1, list2):
	list1 = sorted(list1) 
	list2 = sorted(list2) 

	if list1 == list2:
		return 0
	elif list1 == [] and list1 == []:
		return 0
	else:
		missing = abs(sum(list1) - sum(list2))
		return (missing)