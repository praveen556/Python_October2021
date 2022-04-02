'''
5962. Longest Palindrome by Concatenating Two Letter Words
User Accepted:1125
User Tried:2038
Total Accepted:1136
Total Submissions:3409
Difficulty:Medium
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.



Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".


Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
'''


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        def is_palindrome(word):
            if len(word)==0:
                return False

            start, end = 0, len(word)-1

            while start < end:
                if word[start] != word[end]:
                    return False
                start += 1
                end -= 1

            return True


        stack  = []

        for word in words:
            #Include
            for i in range(len(stack)):
                stack.append(stack[i]+word)

            #Exclude
            stack.append(word)

        output = 0
        for k in stack:
            if is_palindrome(k):
                output = max(output,k)

        return output
