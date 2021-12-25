'''
7. Reverse Integer
Medium

6086

8916

Add to List

Share
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
'''


class Solution:
    def reverse(self, x: int) -> int:

        typ = 1
        if x<0:
            temp = str(x)[1:]
            typ = -1

        else:
            temp =str(x)

        temp = str(temp)[::-1]

        if int(temp)<=-2147483648 or int(temp)>=2147483647:
            return 0

        return int(temp)*typ


'''
Runtime: 28 ms, faster than 90.52% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.2 MB, less than 74.40% of Python3 online submissions for Reverse Integer.
'''
