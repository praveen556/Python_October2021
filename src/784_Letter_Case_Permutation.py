'''
784. Letter Case Permutation
Medium

2634

130

Add to List

Share
Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.



Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: s = "12345"
Output: ["12345"]
Example 4:

Input: s = "0"
Output: ["0"]


Constraints:

s will be a string with length between 1 and 12.
s will consist only of letters or digits.


'''

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        def helper(s, i, slate):
            if i == len(s):
                results.append(slate)
            else:
                if s[i].isdigit():
                    helper(s,i+1,slate+s[i])
                else:
                    helper(s,i+1,slate+s[i].lower())
                    helper(s,i+1,slate+s[i].upper())
        helper(s,0,"")
        return results


'''
As per Leetcode below are specs
Runtime: 52 ms, faster than 89.14% of Python3 online submissions for Letter Case Permutation.
Memory Usage: 15.5 MB, less than 28.27% of Python3 online submissions for Letter Case Permutation.

'''

#Methodd 2 is for better memory utilization

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        def helper(s, i, slate):
            if len(s)==i:
                results.append("".join(slate))
            else:
                if s[i].isdigit():
                    slate.append(s[i])
                    helper(s,i+1,slate)
                    slate.pop()
                else:
                    slate.append(s[i].lower())
                    helper(s,i+1,slate)
                    slate.pop()
                    slate.append(s[i].upper())
                    helper(s,i+1,slate)
                    slate.pop()
        helper(s,0,[])
        return results

'''
Runtime: 64 ms, faster than 51.26% of Python3 online submissions for Letter Case Permutation.
Memory Usage: 15.5 MB, less than 16.09% of Python3 online submissions for Letter Case Permutation.
'''
#Solution 3

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        def helper(s, i):
            if i == len(s):
                results.append(''.join(s))
            else:
                if s[i].isdigit():
                    helper(s,i+1)
                else:
                    s[i]=s[i].lower()
                    helper(s,i+1)
                    s[i]=s[i].upper()
                    helper(s,i+1)
        helper(list(s),0)
        return results

'''
Runtime: 60 ms, faster than 65.13% of Python3 online submissions for Letter Case Permutation.
Memory Usage: 15.5 MB, less than 28.27% of Python3 online submissions for Letter Case Permutation.
'''
