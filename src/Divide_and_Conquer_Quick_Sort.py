class Sort:
#Splitting the Array
    def quicksort(nums, start_index, end_index):
        if start_index < end_index:
            partition_pos = Sort.partition(nums, start_index, end_index)
            Sort.quicksort(nums, start_index, partition_pos - 1)
            Sort.quicksort(nums, partition_pos + 1, end_index)

#Calculating the Position
    def partition(nums, start_index, end_index):
        i = start_index
        j = end_index -1
        pivot = nums[start_index]

        while (i < j):
            while i < end_index and nums[i] < pivot:
                i += 1
            while j > start_index and nums[j] >= pivot:
                j -= 1
            if i < j:
                nums[i] , nums[j] = nums[j], nums[i]
        if nums[i] > pivot:
            nums[i], nums[end_index] = nums[end_index], nums[i]
        return i

arr = [2,1,-1,3,12,76,2,56,1,8]
Sort.quicksort(arr,0, len(arr)-1)
print(arr)
