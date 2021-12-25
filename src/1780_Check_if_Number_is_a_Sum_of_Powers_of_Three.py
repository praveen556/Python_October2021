''''
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.



Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false


Constraints:

1 <= n <= 107

''''




class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            if n % 3 != 0 and (n - 1) % 3 != 0:
                return False
            elif n % 3 != 0:
                return self.checkPowersOfThree((n-1) / 3)
            else:
                return self.checkPowersOfThree(n / 3)


'''
Runtime: 45 ms, faster than 20.00% of Python3 online submissions for Check if Number is a Sum of Powers of Three.
Memory Usage: 14.3 MB, less than 44.31% of Python3 online submissions for Check if Number is a Sum of Powers of Three.
'''
