class Sums:
    def sums_3(nums: list[int], target):
        length, i, dict = len(nums), 0, {}
        Sums.define_target(nums, target)
        while i < length:
            rem = target - nums[i]
            if rem in dict:
                return [dict[rem], i]
            dict[nums[i]]=i
            i+=1
    def define_target(nums: list[int], org_target):
        new_nums = []
        for i in range(len(nums)):
            new_target = org_target - nums[i]
            new_nums.append(org_target-nums[i])
        print(new_nums, new_target)
        #for i in range(len(new_nums)):
        #    Sums.sums_3(new_nums, new_target)
        #return [i, new_nums[i]]

print(Sums.sums_3([3,1,6,2,8,4,5],9))
