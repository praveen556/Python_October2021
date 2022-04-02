def contineous_sub_array(arr):
    if len(arr)<=1:
        return arr
    max_val = 0
    for i in range(len(arr)):
        temp = arr[i]

        for j in range(i,len(arr)):
            temp += arr[j]
            max_val= max(temp,max_val)

    return max_val

print(contineous_sub_array([-2,1,-3,4,-1,2,1,-5,4]))    
