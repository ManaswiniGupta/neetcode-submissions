class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True 
        ps=0
        pr=0
        while ps<len(s) and pr < len(t):
            if s[ps]==t[pr]:
                ps+=1
            pr+=1
        if ps==len(s):
            return True 
        return False
        

        # w=""
        # for i in s:
            
        #     if i in t[t.index(i)+1:]:
        #         w+=i
                
        # return w==s

        # # for i in s:
        # #     if i not in t:
        # #         return False
        #     elif i not in t[t.index(i):]:
        #         return False
        # return True
               

        