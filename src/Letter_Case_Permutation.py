class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        slate = ""
        def Phelper(s, i, slate):
            if i == len(s):
                slate.add("", join(s))
                return slate
            elif s[i].isnumeric:
                Phelper(s[i],i+1,slate)
            else:
                Phelper(s[i].lower(),i+1,slate)
                Phelper(s[i].upper(),i+1,slate)
                return slate

        return [Phelper(s, 0, set())]


print(Solution.letterCasePermutation(1,"a1b2"))
