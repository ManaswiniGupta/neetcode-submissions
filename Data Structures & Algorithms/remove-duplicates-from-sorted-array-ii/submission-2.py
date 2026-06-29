class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l=0
        # r=len(nums)-1
        # while l<r:

        l=[]
        s=Counter(nums)
        for i in s.keys():
            if s[i]<3:
                l.extend([i]*s[i])
            else:
                l.extend([i]*2)
        nums[:] = l
        return len(l)