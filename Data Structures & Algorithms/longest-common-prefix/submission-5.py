class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=strs[0]
        common=""
        for i in range(len(strs)):
            ans=""
            for j in range(len(strs[i])):
                if s[j] :
                    if strs[i][j]==s[j]:
                        ans+=s[j]
                    else:
                        break
                else:
                    break
            common=ans
        return common
            



        