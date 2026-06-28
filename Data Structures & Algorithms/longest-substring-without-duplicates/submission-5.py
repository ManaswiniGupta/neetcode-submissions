class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        ans=0
        charset=set()
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            ans = max(ans, r-l+1)
        return ans



        