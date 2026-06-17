class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[l]=nums[i]
                l+=1
        return l
        # l=[]
        # for i in nums:
        #     if i not in l:
        #         l.append(i)
        # nums[:] = l+nums
        # return len(l)





        