def printunsortedarray(arr,n):
    left = 0
    while left<n-1 and arr[left+1]>arr[left]:
        left+=1

    if left==n-1:
        print("Array is already sorted")
        exit()
    right = n-1
    while right>0 and arr[right] > arr[right-1]:
        right -= 1

    sub_min_val = min(arr[left:right])
    sub_max_val = max(arr[left:right])
    final_left = 0
    while sub_min_val > arr[final_left]:
        final_left += 1

    final_right = n-1
    while sub_max_val < arr[final_right]:
        final_right -= 1

    final_left = min(final_left,left)
    final_right = max(final_right,left)

    return 'Sub Array which needs to be sorted is in between '+ str(final_left) + ' and ' + str(final_right)

#print(printunsortedarray([10,20,30,40,50],5))


print(printunsortedarray([10,35,30,33,30,36,39,40,55,50],10))
