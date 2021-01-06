class Solution:
    def runningSum(nums):
        l=[]
        for i in range(len(nums)):
            l.append(sum(nums[:(i+1)]))
        return l