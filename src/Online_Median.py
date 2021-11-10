'''
Online Median

Given a list of numbers, the task is to insert these numbers into a stream and find the median of the stream after each insertion. If the median is a non-integer, consider it’s floor value.
The median of a sorted array is defined as the middle element when the number of elements is odd and the mean of the middle two elements when the number of elements is even.

Example
Input: [3, 8, 5, 2]
Output: [3, 5, 5, 4]

Iteration
Stream
Sorted Stream
Median
1
[3]
[3]
3
2
[3, 8]
[3, 8]
(3 + 8) / 2 => 5
3
[3, 8, 5]
[3, 5, 8]
5
4
[3, 8, 5, 2]
[2, 3, 5, 8]
(3 + 5) / 2 => 4
Notes
Constraints:
1 <= length of stream <= 10^5.
0 <= any value in the stream <= 10^5.
The stream can contain duplicates.
Custom Input

Input Format:
First-line has the length of the stream.
Then elements of the stream go each on its own line.
Input for “Example” above would look like:

4
3
8
5
2
Output Format:
Each element of the output is printed on its own line.
Output for “Example” above would look like:
3
5
5
4

    Complete the function below.
    The function accepts an INTEGER_ARRAY as parameter and expected to return an INTEGER_ARRAY.
'''
def online_median(stream):
    if len(stream)<=1:
        return stream
    return_list, temp = [], []
    for i in range(len(stream)):
        temp.append(stream[i])
        temp.sort()
        mid = len(temp)//2
        if len(temp)%2==1 or len(temp)==1:
            return_list.append(temp[mid])
        elif len(temp)>2:
            return_list.append((temp[mid]+temp[mid-1])//2)
        else:
            return_list.append((temp[0]+temp[1])//2)
    return return_list
print(online_median([3,8,5,2]))



#2. solution


from heapq import *

# Note: to implement max heap in python, we do 2 operations:
#   1) we multiply the value by one before pushing it to the heap
#   2) we multiploy the value by one after popping it from the heap

def online_median2(stream):
    maxHeap = [] # To store the smaller half of the input numbers.
    minHeap = [] # To store the larger half of the input numbers.

    # Throughout the implementation of heaps below, we maintain heaps balanced so that
    #   1. len(max_heap) = len(min_heap), when number of elements is even
    #   2. len(min_heap) = len(max_heap) + 1, when number of elements is odd

    result = []
    for num in stream:
        if len(minHeap) == len(maxHeap):
            heappush(minHeap, -heappushpop(maxHeap, -num))
            print("Printing Min and Max Heap in Even Criteria",minHeap, maxHeap)
            result.append(minHeap[0])
        else:
            heappush(maxHeap, -heappushpop(minHeap, num))
            print("Printing Min and Max Heap in Odd Criteria",minHeap, maxHeap)
            result.append((minHeap[0]-maxHeap[0]) // 2) # average 2 root values of minHeap and maxHeap

    return result

print(online_median2([3,8,5,2]))
