# def twoNumberSum(array, targetSum):
#    array.sort()
#    answer=list[]
#    left=0
#    right=len(array)-1
#    while left<right:
#       sum=array[left]+array[right]
#       if sum==targetSum:
#          # return[array[left],array[right]]
#          answer.append(array[left])
#          answer.append(array[right])
#       elif sum >targetSum:
#          right-=1
#       elif sum<targetSum:
#          left+=1


#    return answer

def twoNumberSum(array, targetSum):
   array.sort()
   for i in range(len(array)-2):
      left = i+1
      right = len(array)-1
      while left < right:
         currentSum = array[i]+ array[left] + array[right]
         if currentSum == targetSum:
            return [array[i], array[left], array[right]]
         elif currentSum < targetSum:
            left += 1
         elif currentSum > targetSum:
            right -= 1
   return []


print(twoNumberSum([1, 7, 3, 9, 12, 0], 8))
