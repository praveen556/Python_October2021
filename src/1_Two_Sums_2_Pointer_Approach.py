#This Approach is only for sorted List

class Sums:
    def sums_2(nums: list[int], target):
        i,j, return_list =0, len(nums)-1, []
        while i<j:
            if nums[i]+nums[j]>target:
                j-=1
            elif nums[i]+nums[j]<target:
                i+=1
            else:
                #return [i,j] #If index is needed to return
                #return [nums[i],nums[j]] #If values are needed
                return_list.append([nums[i],nums[j]]) #to capture all the combinations
                i+=1
                j-=1 
        return return_list

print(Sums.sums_2([1,2,3,4,5,6],9))
