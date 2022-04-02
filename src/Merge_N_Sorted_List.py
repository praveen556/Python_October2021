def MergeNSortedList(arr):
    if len(arr)<=1:
        return arr
    result = []
    def Merge2lists(arr1, arr2):
        i , j = 0,0
        while i<len(arr1) and j<len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        while len(arr2)!=0 and j<len(arr2):
            result.append(arr2[j])
            j += 1

        while len(arr1)!=0 and i<len(arr1):
            result.append(arr1[i])
            i += 1

    for i in range(0,len(arr),2):
        arr1 = arr[i]
        arr2 = arr[i+1] if (i+1)<len(arr) else []
        print(arr1, arr2)
        Merge2lists(arr1,arr2)

    return result



print(MergeNSortedList([[1,2,3,4],[11,14,16,18],[5,6,7,8],[12,22],[10,13,15,17,19]]))
