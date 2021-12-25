'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.



Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d


Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        w1 = len(word1)
        w2 = len(word2)

        if w1 == 0:
            return word2

        if w2 == 0:
            return word1

        i, j, result = 0, 0, ""
        while True:
            if i<w1 and j<w2:
                result +=(word1[i]+word2[j])
                i+=1
                j+=1
            elif i < w1:
                result += word1[i]
                i+=1
            elif j < w2:
                result +=word2[j]
                j+=1
            else:
                break

        return result

'''
Runtime: 32 ms, faster than 68.38% of Python3 online submissions for Merge Strings Alternately.
Memory Usage: 14.4 MB, less than 15.86% of Python3 online submissions for Merge Strings Alternately.

'''
