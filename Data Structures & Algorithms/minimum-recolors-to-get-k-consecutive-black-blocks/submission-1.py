class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whi = blocks[:k].count("W")
        ans=whi
        for i in range(k,len(blocks)):
            if blocks[i]=="W":
                whi+=1
            if blocks[i-k] == 'W':
                whi -= 1
            ans=min(ans,whi)
        return ans
