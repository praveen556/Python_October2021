'''
6. Zigzag Conversion
Medium

3076

7246

Add to List

Share
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"

'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1:
            return s
        n = len(s)

        result = []
        counter = 2 * numRows-2

        for i in range(numRows):
            for j in range(i,n, counter):
                result.append(s[j])
                if i!=numRows-1 and i!=0 and j+counter-2*i < n:

                    result.append(s[j+counter-2*i])
        newstr = ''.join(result)
        return newstr

  '''
  Runtime: 64 ms, faster than 61.27% of Python3 online submissions for Zigzag Conversion.
  Memory Usage: 14.3 MB, less than 87.81% of Python3 online submissions for Zigzag Conversion.
  '''
