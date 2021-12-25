'''
5. Longest Palindromic Substring
Medium

14649

858

Add to List

Share
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        result, reslen = '', 0
        for i in range(len(s)):
            #odd Length
            left = right = i

            while left>=0 and right <len(s) and s[left] == s[right]:
                if (right-left+1)> reslen:
                    result = s[left:right+1]
                    reslen = right-left+1

                left-=1
                right+=1
            #even Length
            left, right = i, i+1
            while left>=0 and right <len(s) and s[left] == s[right]:
                if (right-left+1)> reslen:
                    result = s[left:right+1]
                    reslen = right-left+1

                left-=1
                right+=1

        return result
