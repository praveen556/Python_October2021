def easy_pass(nums):
    i = 0
    while i < len(nums):
        if nums[i]%2==1:
            i += 1
        else:
            nums.insert(i,nums[i])
            i += 2
    return nums

print(easy_pass([1,2,3,4,5]))
print(easy_pass([5,5,5,5]))
print(easy_pass([2,2]))
print(easy_pass([5,2,1,4,3]))
