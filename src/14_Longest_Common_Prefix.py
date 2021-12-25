
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        l_str = ""
        for word in strs:
            if l_str=="":
                l_str=word
            k = len(l_str)
            i=len(word)
            m=min(k,i)
            while m>=0:
                if m == 0:
                    return ""
                if l_str[:m]==word[:m]:
                    l_str = l_str[:m]
                    break
                m-=1
        return l_str



'''
Runtime: 32 ms, faster than 82.29% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.3 MB, less than 56.10% of Python3 online submissions for Longest Common
'''
