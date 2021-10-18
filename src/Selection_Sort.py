class Sort:
    def Selection(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            min_index = i
            for j in range(i+1,len(nums)):
                if nums[min_index] > nums[j]:
                    min_index = j
            nums[i],nums[min_index] = nums[min_index],nums[i]
        return nums

print(Sort.Selection(1,[1,3,2,4,7,5,4]))

print(Sort.Selection(1,[1,33,22,4,19,5,12]))
