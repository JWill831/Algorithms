# Time O(Nlog(N)+Mlog(M)) because two sorts are happening
def smallestDifference(arrayOne, arrayTwo):
# 	sort each array so we can use pointers
	arrayOne.sort()
	arrayTwo.sort()
# 	set up idx values so we can use while loops
	idxOne=0
	idxTwo=0
# 	intialize the empty answer array
	ans=[]
# 	initialize a running smallest, and a temp for checking each comparison
	smallest=float("inf")
	temp=float("inf")
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
# 		sets our pointers at the begining of each array
		num1=arrayOne[idxOne]
		num2=arrayTwo[idxTwo]
# 		set the temp to the difference of the two pointers
		temp=abs(num1-num2)
# 	check to see if num1 less than num2, and move num1 up one index	because all values to the left are less
		if num1<num2:
			idxOne+=1
# check to see if num1 is more than num2, and move num2 up one index to get num2 closer to num1 value
		elif num1>num2:
			idxTwo+=1
# 			this handles the edge case of if the values are equal, which would be the closest pair
		else:
			return [num1,num2]
# this will update if the temp value is smaller than the current answer, this is the edge case
		if smallest > temp:
			smallest=temp
			ans=[num1,num2]
	return ans

print(smallestDifference([1,-3,5,-11], [27,-7,8,11]))
		
		
		
		
		
		
		
		
	
   
