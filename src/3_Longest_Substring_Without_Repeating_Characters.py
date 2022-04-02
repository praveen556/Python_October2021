import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        left, result, dict = 0, 0, {}

        for i in range(len(s)):

            if s[i] in dict and dict[s[i]] >= left:
                left = dict[s[i]] + 1

            dict[s[i]] = i
            result = max(result, i-left+1)
        return result

print(Solution.lengthOfLongestSubstring(1,"aabdefgabef"))
print(Solution.lengthOfLongestSubstring(1,"abcdefgh"))
print(Solution.lengthOfLongestSubstring(1,"aa"))
print(Solution.lengthOfLongestSubstring(1,"a1a2"))
print(Solution.lengthOfLongestSubstring(1,""))
