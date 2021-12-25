'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
'''

class Solution:
    def calculate(self, s: str) -> int:
        temp = []
        result = 0
        number = 0
        sign = 1

        for c in s:
            if c in '1234567890':
                number = number * 10 + int(c)
            elif c == '+':
                result += sign * number
                number = 0
                sign = 1
            elif c == '-':
                result += sign * number
                number = 0
                sign = -1
            elif c == '(':
                temp.append(result)
                temp.append(sign)
                sign = 1
                result = 0
            elif c == ')':
                result += sign * number

                result *= temp.pop()
                result += temp.pop()
                number = 0

        result += sign * number
        return result
  '''
  Runtime: 60 ms, faster than 99.20% of Python3 online submissions for Basic Calculator.
  Memory Usage: 15.5 MB, less than 61.59% of Python3 online submissions for Basic Calculator.

  '''
