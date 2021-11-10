'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        results = []
        stack = [root]
        while stack:
            rightmost = None
            count = len(stack)
            while count > 0:
                node = stack.pop(0)
                rightmost = node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                count -= 1
            results.append(rightmost)
        return results
