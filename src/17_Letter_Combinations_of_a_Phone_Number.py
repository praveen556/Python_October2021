''''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.





Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz", "0":" "}
        if len(digits) == 1:
            return list(dict[digits[0]])
        temp = self.letterCombinations(digits[:-1])
        add = dict[digits[-1]]
        return [i + j for i in temp for j in add]

'''
Runtime: 32 ms, faster than 64.53% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.2 MB, less than 64.03% of Python3 online submissions for Letter Combinations of a Phone Number.
'''
