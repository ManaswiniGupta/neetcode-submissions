class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={"(":")",
            "[":"]",
            "{":"}"
            }
        for i in s:
            if i in "{[(":
                stack.append(i)
            elif i==d[stack.pop()]:
                pass
            else:
                return False
        return True
