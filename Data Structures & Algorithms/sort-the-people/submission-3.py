class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

         # 1. Combine lists into pairs: [("Mary", 180), ("John", 165), ("Mary", 170)]
        pairs = list(zip(heights, names))
        
        # 2. Sort by height (which is index 1 of the pair) in descending order
        pairs.sort(reverse=True)
        return [name for _, name in pairs]
        

        