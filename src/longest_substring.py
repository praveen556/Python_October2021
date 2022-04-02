import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        left, result, dict = 0, 0, {}

        for i in range(len(s)):

            if s[i] not in dict:
                dict[s[i]] = i
                result = max(result, i-left+1)
            else:
                if dict[s[i]] < left:
                    result = max(result, i-left+1)
                else:
                    left = dict[s[i]] + 1
                dict[s[i]] = i
        return result

print(Solutions.lengthOfLongestSubstring("aabdefgabef"))
print(Solutions.lengthOfLongestSubstring("abcdefgh"))
print(Solutions.lengthOfLongestSubstring("aa"))
print(Solutions.lengthOfLongestSubstring("a1a2"))
print(Solutions.lengthOfLongestSubstring(""))
