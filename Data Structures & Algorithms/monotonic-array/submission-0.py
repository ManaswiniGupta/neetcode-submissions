class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        nums2=sorted(nums)
        if nums==nums2 or nums==nums2[::-1]:
            return True
        return False
        