'''
Palindromic Decomposition Of A String



Find all palindromic decompositions of a given string s.



A palindromic decomposition of string is a decomposition of the string into substrings, such that all those substrings are valid palindromes.



Example

Input: "abracadabra"



Output: [ "a|b|r|a|c|a|d|a|b|r|a", "a|b|r|a|c|ada|b|r|a", "a|b|r|aca|d|a|b|r|a" ]



Notes

Input Parameters: There is only one argument: string s.



Output: Return array of string res, containing ALL possible palindromic decompositions of given string. To separate substrings in the decomposed string, use '|' as a separator between them.

You need not to worry about the order of strings in your output array. Like for s = "aa", arrays ["a|a", "aa"] and ["aa", "a|a"] both will be accepted.
In any string in your returned array res, order of characters should remain the same as in the given string. (i.e. for s = "ab" you should return ["a|b"] and not ["b|a"].)
Any string in the returned array should not contain any spaces. e.g. s = "ab" then ["a|b"] is expected, ["a |b"] or ["a| b"] or ["a | b"] will give the wrong answer.


Constraints:

1 <= |s| <= 20
s only contains lowercase letters ('a' - 'z').


Any string is its own substring.



Custom Input

Input Format: The first and only line of input should contain a string s, denoting the input string. If s = “abracadabra”, then input should be: abracadabra



Output Format: Let’s denote size of res array as m, where res is the resultant array of string returned by solution function.

Then, there will be m lines of output, where ith line contains a string res[i], denoting string at index i of res.

For input s = “abracadabra”, output will be:

a|b|r|a|c|ada|b|r|a

a|b|r|aca|d|a|b|r|a

a|b|r|a|c|a|d|a|b|r|a

'''


def generate_palindromic_decompositions(string):
    if not string or len(string) == 1:
        return [string]

    output = []
    n = len(string)

    def _palindromic_decomposition(so_far, start):
        # base case
        if start == n:
            output.append('|'.join(so_far))
            return

        # take every possible string from the current position and
        # if it's palndromic go forward, and if it's not prune
        for i in range(start+1, n+1):
            curr = string[start:i]
            if is_palindrome(curr):
                so_far.append(curr)
                _palindromic_decomposition(so_far, i)
                # at the end of dfs remove what was appended to
                so_far.pop()

    _palindromic_decomposition([], 0)
    return output


def is_palindrome(string):
    if not string or len(string) == 1:
        return True

    low, high = 0, len(string) - 1
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1

    return True


def is_palindrome_rec(string):
    if len(string) == 0:
        return True
    return _is_palindrome(string, 0, len(string)-1)


def _is_palindrome(string, start, end):
    # empty string or string of 1 character
    if start == end or start > end:
        return True

    return string[start] == string[end] and _is_palindrome(string, start+1, end-1)
