'''
Generate All Subsets Of A Set

Generate ALL possible subsets of a given set. The set is given in the form of a string s containing distinct lowercase characters 'a' - 'z'.

Example

Input: "xy"

Output: ["", "x", "y", "xy"]

Notes

Input Parameters: There is only one argument denoting string s.

Output: Return array of strings res, containing ALL possible subsets of given string. You need not to worry about order of strings in your output array. E.g. s = "a", arrays ["", "a"] and ["a", ""]  both will be accepted.

Order of characters in any subset must be same as in the input string. For s = "xy", array ["", "x", "y", "xy"] will be accepted, but ["", "x", "y", "yx"] will not be accepted.

Constraints:

0 <= |s| <= 19
s only contains distinct lowercase alphabetical letters ('a' - 'z').
Empty set is a subset of any set.

Any set is a subset of itself.

Custom Input

Input Format: The first and only line of input should contain a string s, denoting the input string.

If s = “xy”, then input should be: xy

Output Format: Let’s denote the size of res as m, where res is the resultant array of strings returned by the solution function.

Then, there will be m lines of output, where ith line contains string at index i of res.

For input s = “xy”, output will be:

----------- START of output -----------

x

y

xy

----------- END of output ---------------

(Note that the first line is an empty line, corresponding to empty set [“”].)

'''

# Complete the function below.

def generate_all_subsets(s):
    results = []
    def helper(s, i, slate):
        if i == len(s):
            results.append(''.join(slate[:]))
        else:
            #Exclusion
            helper(s, i+1, slate)
            #Inclusion
            slate.append(s[i])
            helper(s,i+1,slate)
            slate.pop()
    helper(s, 0, [])
    return results


# Approach 2 using Libraries.


# Complete the function below.

def generate_all_subsets(s):
    results = []
    def helper(slate, i):
        if i == len(s):
            results.append(''.join(slate))
            return
        else:
            #Include Case
            helper(slate + [s[i]], i+1)
            #Exclude Case
            helper(slate, i+1)
    helper([],0)
    return results
