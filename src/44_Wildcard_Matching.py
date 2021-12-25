'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input: s = "acdcb", p = "a*c?b"
Output: false
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p)==1 and p[0]=='*':
            return True

        n=len(s)
        m=len(p)
        result=[[False]*(m+1) for _ in range(n+1)]

        result[-1][-1]=True
        for j in range(m-1,-1,-1):
            if p[j]=="*":
                result[-1][j]=True
            else:
                break

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if s[i]==p[j] or p[j]=="?":
                    result[i][j]=result[i+1][j+1]
                elif p[j]=="*":
                    result[i][j]=(result[i][j+1] or result[i+1][j])
                else:
                    result[i][j]=False
        return result[0][0]

  '''
  Runtime: 708 ms, faster than 65.54% of Python3 online submissions for Wildcard Matching.
  Memory Usage: 22.6 MB, less than 59.84% of Python3 online submissions for Wildcard Matching.
  '''
