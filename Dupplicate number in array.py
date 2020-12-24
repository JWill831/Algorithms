

def firstDuplicateValue(array):
	seen={}
	for i in array:
		if i in seen:
			return i
		else:
			seen[i]=True
	return -1

print(firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]))
