'''
Equal Sub Set Partition



Given an array s of n integers, partition it into two non-empty subsets, s1 and s2, such that the sum of all elements in s1 is equal to the sum of all elements in s2. Return a boolean array of size n where i-th element is True if i-th element of s belongs to s1 and False if it belongs to s2. Any valid answer will be accepted. If such partitioning is not possible, return an empty array.



Example

Input: n = 6, s = [10, -3, 7, 2, 1, 3]

Output: [True, True, False, False, False, True]



There are multiple partitionings where s1 sums up to 10 and s2 sums up to 10; they are all correct answers:

s1 = [ 10 , -3 , 3 ] and s2 = [ 7 , 2 , 1 ] (Sample output)
s1 = [ 7 , 2 , 1 ] and s2 = [ 10 , -3 , 3 ]
s1 = [10] and s2 = [-3, 3, 7, 2, 1]
s1 = [-3, 3, 7, 2, 1] and s2 = [10]
s1 = [10, -3, 2, 1] and s2 = [7, 3]
s1 = [7, 3] and s2 = [10, -3, 2, 1]


Notes

Input Parameters: The first and only parameter of the function that is to be implemented is the array of integers s, that is to be partitioned.



Output Format: If it is possible to partition the given array s in an above-said manner then return a boolean array of size n, where its i (0<=i<N) element is true if it is the part of s1 else false if it is the part of s2. In case it is not possible to partition the array s, then return an empty array.



Constraints:

1 <= n <= 100
-100 <= elements in s <= 100


Custom Input

Input Format: The first line of the text file contains one single integer n, denoting number of elements in array s.

Next n lines of the input, each line contains a single integer denoting the ith element in the array s.

If n = 3 and s = [1, 0, -1], then custom input format will be:

3

1

0

-1



Output Format: If a valid partition exists, then the first line contains an integer s1, denoting the size of the first subset and next S1 line contains

i-th elements in the set s1 in the order they appear in the input array s. Next line contains an integer s2, denoting the size of the second subset. Next s2 lines will contain integers denoting the ith element in the set s2 in the order they appear in the input array s.

In case a valid partition is not possible the output contains only one line having integer -1.

For the above-provided custom input, one possible custom output could be:

2

1

-1

1

0
'''


#
#  Complete the equalSubSetSumPartition function below.
#
#  @param s: input array as parameter.
#
def equalSubSetSumPartition(s):
    # Write your code here
    n= len(s)
    if n<=1 or sum(s)%2!=0:
        return []

    results = [False]*n

    target = sum(s)//2

    buffer =[set() for _ in range(n)]
    buffer[0].add(s[0])

    if target in buffer[0]:
        results[0]= True
        return results
    found = None

    for i in range(1, n-1):
        buffer[i]=buffer[i-1].copy()
        buffer[i].add(s[i])
        for possible_sum in buffer[i-1]:
            buffer[i].add(possible_sum + s[i])
        if target in buffer[i]:
            found = i
            break
    if found == None:
        return []
    answer_i = found
    while answer_i >= 0:
        if answer_i == 0:
            if target == s[answer_i]:
                results[answer_i] = True
                return results
            return results
        if target in buffer[answer_i] and target not in buffer[answer_i - 1]:
            results[answer_i] = True
            target -= s[answer_i]
        answer_i -= 1
print(equalSubSetSumPartition([10, -3, 7, 4, 1, 3]))
