class Solution:
    def minOperations(self, s: str) -> int:
        ans=0
        a=s[0]
        if len(s)<2:
            return 0
        for i in range(0,len(s),2):
            if s[i+1]:
                if s[i]==s[i+1]:
                    ans+=1
        return ans