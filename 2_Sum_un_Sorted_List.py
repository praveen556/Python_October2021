class Sum:
    def sums_2(self, nums: list[int], target) -> list[int]:
        dict, return_list ={}, []
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in dict:
                return_list.append([dict[rem],i])
            dict[nums[i]]=i
        return return_list

print(Sum.sums_2(1,[3,1,6,2,8,4,5],9))
