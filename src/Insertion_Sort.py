class Sort:
    def Insertion(self, nums: list[int]) -> list[int]:
        length = len(nums)
        for i in range(length):
            temp = nums[i]
            j = i-1
            while j>=0 and nums[j] > temp:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = temp
        return nums

print(Sort.Insertion(1,[8,2,4,9,3,6]))
