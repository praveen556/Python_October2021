'''
Word Break Count



Given a dictionary of words and a string, find the number of ways the string can be broken down into the dictionary words. Return the answer modulo 10^9 + 7.



Example

Input: Dictionary: [“kick", "start", "kickstart", "is", "awe", "some", "awesome”]. String: “kickstartisawesome”.

Output: 4

Here are all four ways to break down the string into the dictionary words:

kick start is awe some
kick start is awesome
kickstart is awe some
kickstart is awesome
4 % 1000000007 = 4 so the correct output is 4.



Notes

Input Parameters: Function has two parameters. 1) an array of strings, the dictionary, 2) a string to be broken down in dictionary words.



Output: Return an integer, the number of distinct ways to break down the string into the dictionary words modulo 10^9 + 7.



Constraints:

1 <= number of words in the dictionary <= 200000
1 <= length of any dictionary word <= 100
1 <= length of the string <= 2000
Dictionary words and the string all consist of lowercase latin characters (no whitespace, in particular).


Custom Input

Input Format:

The first line of the input contains one single integer denoting dictionaryCount, the number of words in our dictionary.

Next dictionaryCount lines contain strings denoting words in our dictionary. Next line contains one single string denoting the txt string.

If dictionaryCount = 2 , dictionary = [“hello” , “world”] and

txt = “helloworld” then custom input format will be:

2

hello

world

helloworld



Output Format: Print one integer denoting all different possible word-break arrangements for the txt string.

For the above-provided custom input, output there is only one way to partition the txt string ( “hello world”), so the output will be:

1

'''

#
# Complete the 'wordBreakCount' function below.
#
# The function accepts STRING_ARRAY dictionary as parameter
# and the original STRING txt on which segmentation is to be
# performed.
# The function returns the count of all possible segmentation
#

from collections import *
def wordBreakCount(dictionary, txt):
    # Write your code here
    #Convert list to dictionary
    wordCounts = set(len(word) for word in dictionary)
    wordSet = set(dictionary)
    counts = [0]*(len(txt)+1)
    counts[0] = 1

    for i in range(1, len(txt)+1):
        for wordCount in wordCounts:
            if wordCount<=i:
                if txt[i-wordCount:i] in wordSet:
                    counts[i] +=counts[i-wordCount]
    return counts[-1] % (pow(10,9) + 7)

print(wordBreakCount(["kick", "start", "kickstart", "is", "awe", "some", "awesome"],"kickstartisawesome"))
