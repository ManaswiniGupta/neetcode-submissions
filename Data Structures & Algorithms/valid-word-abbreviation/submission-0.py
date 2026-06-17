class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l=0
        r=0
        while l<len(word) and r<len(abbr):
            if word[l]==abbr[r]:
                l+=1
                r+=1
            elif abbr[r].isalpha():
                return False
            elif abbr[r].isdigit():
                if abbr[r]=='0':
                    return False
                tem=0
                while r<len(abbr) and abbr[r].isdigit():
                    tem=tem*10+int(abbr[r])
                    r+=1
                l+=tem

        return l == len(word) and r == len(abbr)



        # for i in range(len(abbr)):
        #     if str(abbr[i]):
        #         if word[l]!=abbr[i]:
        #             return False
        #     elif int(abbr[i]):
        #         l+=int(abbr[i])
        #     else:
        #         l+=1
        # return True


        