'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
'''



class Solution:
    def maxArea(self, height: List[int]) -> int:

        if len(height)==0:
            return 0
        area, i, j = 0, 0, len(height)-1

        while i < j:
            area = max(area, (min(height[i],height[j])*(j-i)))

            if height[i]<height[j]:
                i+=1
            else:
                j-=1

        return area




    '''
    Runtime: 740 ms, faster than 69.56% of Python3 online submissions for Container With Most Water.
    Memory Usage: 27.5 MB, less than 75.51% of Python3 online submissions for Container With Most Water.
    '''


class Solution:
    def maxArea(self, height: List[int]) -> int:

        if len(height)==0:
            return 0
        area, i, j = 0, 0, len(height)-1

        while i < j:

            if height[i]<height[j]:
                area = max(area,height[i]*(j-i))
                i+=1
            else:
                area = max(area, height[j]*(j-i))
                j-=1

        return area

'''
Runtime: 684 ms, faster than 91.24% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.7 MB, less than 23.03% of Python3 online submissions for Container With Most Water.
'''
