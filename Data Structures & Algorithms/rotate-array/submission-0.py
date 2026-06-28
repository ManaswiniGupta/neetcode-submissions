class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=0
        while r+k<len(nums):
            nums[r+k],nums[l] = nums[l], nums[r+k]
            r+=1
            l+=1
        return nums

        