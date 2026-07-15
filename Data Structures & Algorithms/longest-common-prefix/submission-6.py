class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix
        




























        # s=strs[0]
        # common=""
        # for i in range(len(strs)):
        #     ans=""
        #     for j in range(len(strs[i])):
        #         if s[j]:
        #             if strs[i][j]==s[j]:
        #                 ans+=s[j]
        #             else:
        #                 break
        #         else:
        #             break
        #     common=ans
        # return common
            



        