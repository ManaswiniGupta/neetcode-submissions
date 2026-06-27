class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l=0
        count = customers[0] if grumpy[0]==0 else 0
        # customers[i] if grumpy[i] == 0 else 0
        if len(customers)>minutes:
            window=sum(customers[:minutes])
        else:
            return sum(customers)
        maxi=0
        for i in range(1,len(customers)):
            if grumpy[i]==0:
                count+=customers[i]
            maxi = max(window,maxi)
            
            window = window + customers[i+minutes-1] - customers[i-1]
            # maxi = max(window,maxi)
        return count+maxi
        

            
