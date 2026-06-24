class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans=100000
        nums.sort()
        i=0
        while i+k<=len(nums):
            ans = min(ans, nums[i+k-1]-nums[i])
            i+=1
        return ans
        