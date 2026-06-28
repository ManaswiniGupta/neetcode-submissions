class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        window=[s[0]]
        if s=="":
            return 0
        m=1
        for i in range(1,len(s)):
            r = set(window)
            if s[i] not in r:
                window+=s[i]
            else:
                while s[i] in r and window:
                    window.pop(0)
            m=max(m,len(window))
        return m


        