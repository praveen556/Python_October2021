"""
Given an initial list along with another list of numbers to be appended with the initial list and an integer K, return an array consisting of the Kth largest element after adding each element from the first list to the second list.

Example
Input: [ 2, [4, 6], [5, 2, 20] ]
Output: [5, 5, 6]

Append
Stream
Sorted Stream
2nd largest
5
[4, 6, 5]
[4, 5, 6]
5
2
[4, 6, 5, 2]
[2, 4, 5, 6]
5
20
[4, 6, 5, 2, 20]
[2, 4, 5, 6, 20]
6

Notes
Constraints:
1 <= length of both lists <= 10^5.
1 <= K <= length of initial list + 1.
0 <= any value in the list <= 10^9.
The stream can contain duplicates.
Custom Input
Input Format:
- First-line contains the value of K.
- Second-line has the length of the initial list.
- Then elements of the initial list go each on its own line.
- The next line has the length of another list.
- Then elements of another list go each on its own line.
Input for “Example” above would look like:
2
2
4
6
3
5
2
20
Output Format:
- Each element of the output is printed on its own line.
Output for “Example” above would look like:
5
5
6
"""
#
# The function accepts an INTEGER and two INTEGER_ARRAYS as parameters and
# is expected to return an INTEGER_ARRAY.
#
import heapq
def kth_largest(k, initial_stream, append_stream):
    # Write your code here
    return_list = []
    heapq.heapify(initial_stream)

    for i in range(len(initial_stream)-k):
        heapq.heappop(initial_stream)

    for i in append_stream:
        if len(initial_stream)<k:
            heapq.heappush(initial_stream, i)

        elif i>initial_stream[0]:
            heapq.heappushpop(initial_stream, i)

        return_list.append(initial_stream[0])

    return return_list

kth_largest(2,[4,6],[5,2,20])
