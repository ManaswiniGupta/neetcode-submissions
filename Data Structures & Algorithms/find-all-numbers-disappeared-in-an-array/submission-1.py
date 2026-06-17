class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(1,n+1):
            if i not in nums:
                ans.append(i)
        return ans
        