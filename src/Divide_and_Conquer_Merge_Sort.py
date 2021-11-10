class Sort:
    def Helper(mrg_nums: list[int]):
        #Recurssive Phase
        if len(mrg_nums)>1:
            left_array = mrg_nums[:len(mrg_nums)//2] #This is for Left 0 to Middle array
            right_array = mrg_nums[len(mrg_nums)//2:] #This is for Middle of array to End of array

            Sort.Helper(left_array)
            Sort.Helper(right_array)
            i, j, k = 0, 0, 0
            #Merging Phase
            while i <= len(left_array)-1 and j <= len(right_array)-1:
                if left_array[i] <= right_array[j]:
                    mrg_nums[k] = left_array[i]
                    i += 1
                else:
                    mrg_nums[k] = right_array[j]
                    j += 1
                k += 1
            #Gather Phase
            while i <= len(left_array)-1:
                mrg_nums[k] = left_array[i]
                i += 1
                k += 1
            while j <= len(right_array)-1:
                mrg_nums[k] = right_array[j]
                j += 1
                k += 1
            return mrg_nums
        return mrg_nums

print(Sort.Helper([2,1,-1,3,12,76,2,56,1,8]))
