class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=Counter(nums)
        ans=0
        for i in c.values():
            if i%2==0 and i%3==0:
                ans+=i//3
            elif  i%2!=0 and i%3==0:
                ans+=i//3
            elif i%2==0 and i%3!=0:
                ans+=i//2
            else:
                return -1
        return ans
        