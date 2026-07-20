class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=-1
        c=Counter(s)
        for i in range(len(s)):
            if c[s[i]]==1:
                a=i
                break
        return a


                
        