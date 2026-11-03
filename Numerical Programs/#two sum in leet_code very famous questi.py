#two sum in leet_code very famous question in interview and also 1st question in leet_code problems
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        for i in range(0,(n-1)):
            for j in range((i+1),n):
                if nums[i]+nums[j]==target:
                    return [i,j]
#2nd logic 
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict={}
        for i in range(0,len(nums)):
            x=target-nums[i]
            if x in dict:
                return [dict[x],i]
            else:
                dict[nums[i]]=i