class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # d={}
        # s="balloon"
        # for i in s:
        #     if i not in text:
        #         return False
        # for i in text:
        #     d[i]=d.get(i,0)+1
        # ans=min(d["b"],d["a"],d["l"],d["o"],d["n"])
        
        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        return res
            

        