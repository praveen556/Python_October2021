'''
Kth Largest In An Array
Given an array of integers, find the kth largest number in it.
Example One:
Input: [5, 1, 10, 3, 2], 2
Output: 5
Example Two:
Input: [4, 1, 2, 2, 3], 4
Output: 2
Notes:
Constraints:
1 <= Array Size <= 3*105.
-109 <= Array Elements <= 109.
1 <= k <= Array Size.
Custom Input:

Input Format:
The first line contains the array size. The elements of the array are then listed, one in each line. Last line contains the value of k.
Input from “Example One” above would look like this:

5
5
1

10
3
2
2

Output Format:
Output contains the kth largest element in the array.
Output from “Example One” above would look like this:
5

'''
'''
   Complete the function below.
   The function takes an INTEGER ARRAY and an INTEGER as inputs and is expected to return an INTEGER.
'''
import heapq
def kth_largest_in_an_array(numbers, k):
    heapq.heapify(numbers)
    for i in range(len(numbers)-k):
        heapq.heappop(numbers)
    return numbers[0]
