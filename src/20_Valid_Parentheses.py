'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


class Solution:
    def isValid(self, s: str) -> bool:

        buffer = []
        dict = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in dict.values():
                buffer.append(char)

            elif char in dict.keys():
                if buffer==[] or dict[char] != buffer.pop():
                    return False
            else:
                return False

        return buffer == []



'''
Runtime: 28 ms, faster than 86.25% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.5 MB, less than 7.83% of Python3 online submissions for Valid Parentheses.

'''
