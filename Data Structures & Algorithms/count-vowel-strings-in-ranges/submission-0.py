class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        l=[]
        def check(s):
            v="aeiou"
            if s[0] in v and s[-1] in v:
                return True
            return False
        for i in range(len(queries)):
            c=0
            for k in words[queries[i][0]:queries[i][1]+1]:
                if check(k)==True:
                    c+=1
            l.append(c)
        return l
                 
        