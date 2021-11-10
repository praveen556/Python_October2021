"""
Top K Frequent Elements
Given an integer array and a number k, find the k most frequent elements in the array.

Example One
Input: [1, 2, 3, 2, 4, 3, 1], 2
Output: [3, 1]

Example Two

Input: [1, 2, 1, 2, 3, 1], 1
Output: [1]

Notes
If multiple answers exist, return any.
The order of numbers in the output array does not matter.

Constraints:
1 <= Array Length <= 3*105.
1 <= k <= Unique elements in the input array.
0 <= Any element in the input array <= 3*105.
Custom Input

Input Format:
The first line contains the size of the input array.
Then the numbers of the array are listed, one in each line.
The last line contains a number denoting k.
Input from “Example One” above would be:

7
1
2
3
2
4
3
1
2

Output Format:
The output should contain k lines where each line will have a single integer.
Output from “Example One” above would be:

3
1
"""

def find_top_k_frequent_elements(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    temp, freq, l = [], {}, 1
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    freq2 = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))
    for i in freq2:
        if  l <= k:
            temp.append(i)
        l+=1
    return temp


print(find_top_k_frequent_elements([4,4,3,5,5],2))


#2nd Method
from collections import Counter
import heapq
def find_top_k_frequent_elements_easy(arr,k):
    freq = Counter(arr)
    return heapq.nlargest(k, freq.keys(), key=freq.get)
print(find_top_k_frequent_elements_easy([4,4,3,5,5],2))
