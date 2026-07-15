class Solution:
    def compress(self, chars: List[str]) -> int:
        ans=""
        l=0
        r=0
        while r<len(chars):
            count=0
            while  r<len(chars) and chars[l]==chars[r]:
                count+=1
                r+=1
            if count==1:
                ans+=chars[l]
            else:
                ans+=chars[l]+str(count)
            l=r
        for i in range(len(ans)):
            chars[i] = ans[i]
        return len(ans)
            
            
            