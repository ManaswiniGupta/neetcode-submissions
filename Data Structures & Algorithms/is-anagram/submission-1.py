class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for i in s:
            d[i]=d.get(i, 0)+1
        for j in t:
            if j in d.keys():
                d[j]-=1
            else:
                return False
        for i in d.values():
            if i>0:
                return False
        return True 
        