class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        window_sum=sum(arr[:k])
        count=0
        while k+l<=len(arr):
            if window_sum >= threshold * k:
                count+=1
            if k + l < len(arr):
                window_sum += arr[k + l] - arr[l] 
            l+=1
        return count
            

        