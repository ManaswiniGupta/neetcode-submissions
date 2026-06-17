class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        ans=0
        for i in nums:
            if i==1:
                maxi+=1
                ans=max(maxi, ans)
            else:
                maxi=0
        return ans
