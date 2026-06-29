class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # ans=0
        # k=[fruits[0]]
        # for i in range(1,len(fruits)):
        #     if len(set(k))<3:
        #         k+=[fruits[i]]
        #         ans=max(ans,len(k))
        #     else:
        #         k.pop(0)
            
        # return ans

        c=defaultdict(int)
        l=0
        for r in range(len(fruits)):
            count[fruits[r]]+=1    

            if len(count)>2:
                count[fruits[[l]]]-=1
                if count[fruits[l]]==0:
                    count.pop(fruits[l])
                l+=1
        return len(fruits)-l