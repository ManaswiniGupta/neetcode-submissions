class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans=0
        for i in s[::-1].lstrip():
            if i.isalnum():
                ans+=1
            else:
                break
        return ans
        