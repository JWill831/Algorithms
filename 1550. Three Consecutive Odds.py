# 1550. Three Consecutive Odds
# Easy

# 102

# 14

# Add to List

# Share
# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

# Example 1:

# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
# Example 2:

# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.
 

# Constraints:

# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000

def threeConsecutiveOdds(arr):
    for i in range(0,len(arr)):
        arr[i]=arr[i]%2
    for i in range(0,len(arr)-2):
        if(arr[i]==1 & arr[i+1]==1 & arr[i+2]==1):
            return True
    return False

print(threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))