class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i=0
        ans=101
        while i+k<=len(blocks):
            w=Counter(blocks[i:i+k+1])
            ans = min(ans,w["W"])
            i+=1
        return ans

        