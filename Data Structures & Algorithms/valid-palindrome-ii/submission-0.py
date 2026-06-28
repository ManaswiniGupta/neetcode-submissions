class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        c=1
        while l<r:
            if s[l]==s[r]:
                r-=1
                l+=1
            elif c!=0:
                if s[r-1]==s[l]:
                    c-=1
                    r-=1
                elif s[l+1]==s[r]:
                    c-=1
                    l+=1
                else:
                    return False
        return True


        