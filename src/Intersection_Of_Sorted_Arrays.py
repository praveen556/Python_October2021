from heapq import *
#
# Complete the function below.
#
# The function accepts three INTEGER_ARRAY arr1, arr2, arr3 as parameter and expected to return an INTEGER_ARRAY.
#

def find_intersection(arr1, arr2, arr3):
    # Write your code here
    if (len(arr1)==0) or (len(arr2)==0) or (len(arr3)==0):
        return -1
    i, j, k, result_list = 0, 0, 0, []
    while i < len(arr1) and j <len(arr2) and k < len(arr3):
        if arr1[i]==arr2[j]==arr3[k]:
            result_list.append(arr1[i])
            i+=1
            j+=1
            k+=1
        elif arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr3[k]:
            j+=1
        else:
            k+=1
    if len(result_list)==0:
        return -1
    else:
        return result_list
