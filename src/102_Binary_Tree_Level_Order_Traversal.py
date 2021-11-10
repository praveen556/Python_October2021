'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

#Approach 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue =deque()
        queue.append(root)
        results = []

        while queue:
            temp = []
            count = len(queue)

            while count > 0:
                node = queue.popleft()
                temp.append(node.val)
                count -= 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(temp)
        return results

#Appraoch 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        results = []

        while queue:
            temp = []
            count = len(queue)

            while count > 0:
                node = queue.pop(0)
                temp.append(node.val)
                count -= 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(temp)
        return results
