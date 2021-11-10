'''

31. Next Permutation


Add to List

Share
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        maxi=nums[-1] #initilize maxi


        for i in range(len(nums)-1,-1,-1):
            if(nums[i]<maxi):#checking if there is any element towards right tht is greater than present element
                nums[i+1:]=sorted(nums[i+1:])# sort the right side from i+1 position
                j=i+1
                while(nums[i]>=nums[j]  ):#find the next greater integer to nums[i]
                    j+=1
                nums[i],nums[j]=nums[j],nums[i]# replace the element with next greater integer
                return
            maxi=max(maxi,nums[i])#updating the maximum element present on right side

        # if the list is reverse sorted
        nums.sort()
        return 

Solution.nextPermutation(1,[1,2,3])

Solution.nextPermutation(1,[3,2,1])

Solution.nextPermutation(1,[1,1,5])

Solution.nextPermutation(1,[1])
