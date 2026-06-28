class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=strs[0]
        common=""
        for i in range(len(strs)):
            ans=""
            for j in range(len(strs[i])):
                if strs[i][j]==s[j] and strs[i][j]:
                    ans+=s[j]
                else:
                    break
            common=ans
        return common
            



        