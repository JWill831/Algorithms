def threeNumberSum(array, targetSum):

	array.sort()
	ans=[]
	for i in range(len(array)-2):
		left = i+1
		right= len(array) - 1
		while left < right:
			temp=array[i]+array[left]+array[right]
			if temp==targetSum:
				ans.append([array[i],array[left],array[right]])
				left+=1
				right-=1
			elif temp>targetSum:
					right -= 1
			elif temp<targetSum:
					left += 1
	return ans