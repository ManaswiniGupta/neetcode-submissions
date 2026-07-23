class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=[]
        nums.sort()
        for i in range(len(nums)):
            if i+1!= nums[i]:
                l.append(i)
                l.append(i+1)
        return l
