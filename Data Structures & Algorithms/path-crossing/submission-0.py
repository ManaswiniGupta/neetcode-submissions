class Solution:
    def isPathCrossing(self, path: str) -> bool:
        c=Counter(path)
        for i in c.values():
            if i>1:
                return True
        return False
        