class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=10*5
        k=0
        window=[]
        for i in range(1,len(nums)): 
            window.append(nums[i])
            while sum(window)>=target:   
                ans=min(ans,len(window))
                window.pop(0)
            
        if ans==10*5:   
            return 0    
        return ans
        