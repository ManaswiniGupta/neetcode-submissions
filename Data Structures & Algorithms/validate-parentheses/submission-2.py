class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={"(":")",
            "[":"]",
            "{":"}"
            }
        if len(s)<2:
            return False
        for i in s:
            if i in "{[(":
                stack.append(i)
            elif stack and i==d[stack.pop()]:
                pass
            else:
                return False
        return True
