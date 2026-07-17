class Solution:
    def isPathCrossing(self, path: str) -> bool:
        c=Counter(path)
        if path in ["EW","NS","WE","SN"]:
            return True
        for i in c.values():
            if i>1:
                return True
        return False
        