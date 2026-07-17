class Solution:
    def isPathCrossing(self, path: str) -> bool:
        c=Counter(path)
        d= ["EW","NS","WE","SN"]
        for j in d:
            if j in path:
                return True
        for i in c.values():
            if i>1:
                return True
        return False
        