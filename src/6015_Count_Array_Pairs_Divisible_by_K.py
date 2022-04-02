import itertools
class Solution:
    def coutPairs(self, nums: list[int], k: int) -> int:
        result = 0

        d_temp = itertools.combinations(nums, 2)
        print(d_temp)
        for i in d_temp:
            if (i[0]*i[1])%k==0:
                result += 1

        return result

'''
        result = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i]*nums[j])%k==0:
                    result += 1

        return result
'''

print(Solution.coutPairs(1,[1,2,3,4,5],2))
