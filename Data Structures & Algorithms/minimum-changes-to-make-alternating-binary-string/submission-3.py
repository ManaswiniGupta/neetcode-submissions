class Solution:
    def minOperations(self, s: str) -> int:
        d=Counter(s)
        ans=0
        if len(s)<2:
            return 0
        if len(s)%2==0:
            ans=abs(d["1"]-d["0"])/2
            return int(ans)
        else:
            for i in range(0,len(s)-1,2):
                if s[i+1]:
                    if s[i]==s[i+1]:
                        ans+=1
            if s[0]==s[-1]:
                return ans
            return ans+1

            
        # ans=0
        # a=s[0]
        # if len(s)<2:
        #     return 0
        # for i in range(0,len(s),2):
        #     if s[i+1]:
        #         if s[i]==s[i+1]:
        #             ans+=1
        # return ans