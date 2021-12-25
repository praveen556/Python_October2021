'''
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''


class Solution:
    def calculate(self, s: str) -> int:
        if len(s)==1 and s.isdigit():
            return s
        s = s.replace(" ", "")

        temp = 0
        last  = '+'
        result = []

        for char in s:
            if char in '+-*/':
                if last=='+':
                    result.append(temp)
                elif last == '-':
                    result.append(-temp)
                elif last == '*':
                    result.append(result.pop()*temp)
                else:
                    result.append(int(result.pop()/temp))
                temp = 0
                last = char
            else:
                temp = (temp*10) + int(char)
        if last=='+':
            result.append(temp)
        elif last=='-':
            result.append(-temp)
        elif last == '*':
            result.append(result.pop()*temp)
        else:
            result.append(int(result.pop()/temp))

        return sum(result)



'''
Runtime: 68 ms, faster than 94.13% of Python3 online submissions for Basic Calculator II.
Memory Usage: 16.5 MB, less than 17.67% of Python3 online submissions for Basic Calculator II.
Next challen
'''
