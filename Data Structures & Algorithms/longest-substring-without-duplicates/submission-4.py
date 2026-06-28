class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        if s=="":
            return 0
        window=s[0]
        m=1
        for i in range(1,len(s)):
            if s[i] not in window:
                window+=s[i]
            else:
                while s[i] in window and window:
                    window=window[1:]
            m=max(m,len(window))
        return m
                



        