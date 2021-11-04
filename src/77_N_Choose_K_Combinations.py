'''
N Choose K Combinations

Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.

Example One:

Input: 5, 2

Output: [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]].

Example Two:

Input: 6, 6
Output: [[1, 2, 3, 4, 5, 6]].

Notes:

The answer can be returned in any order.

Constraints:

1 <= n <= 20
1 <= k <= n
Custom Input:

Input Format:

The first line of input contains the integer n.
The second line of input contains the integer k.
Input from “Example One” above would look like this:

5

2

Output Format:

The output contains the unique combinations, one in each line.
The integers within a combination are printed in a space-separated manner.
Output from “Example One” above would look like this:

1 2

1 3

1 4

1 5

2 3

2 4

2 5

3 4

3 5

4 5

'''



'''
    Complete the function below.
    The function takes two INTEGERS as inputs and is expected to return an INTEGER 2D ARRAY.
'''
def find_combinations(n, k):
    results = []
    def helper(n, i, k, slate):
        #Backtracking
        if len(slate) == k:
            results.append(slate[:])
            return
        #Base Case
        if i == n+1:
            return
        else:
            helper(n, i+1, k, slate) #Exclusion
            #Inclusion
            slate.append(i)
            helper(n, i+1,k, slate)
            slate.pop()
    helper(n, 1, k, [])
    return results


#Solution 2


'''
    Complete the function below.
    The function takes two INTEGERS as inputs and is expected to return an INTEGER 2D ARRAY.
'''
from itertools import combinations
def find_combinations(n, k):
    return list(combinations(list(range(1, n+1)), k))
