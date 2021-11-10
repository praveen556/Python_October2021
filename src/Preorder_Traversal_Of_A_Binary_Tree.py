'''
Preorder Traversal Of A Binary Tree

Given a binary tree, find the preorder traversal of its nodes’ labels.

Example One

Input:



Output: [ 0, 1, 3, 4, 2 ]

Example Two:

Input:



Output: [ 0, 1, 2, 3 ]

Notes:

The preorder traversal processes all the nodes of a binary tree by first visiting the root, then recursively visiting its left and right subtrees respectively.

Constraints:

1 <= Number of nodes in the binary tree <= 20000.
The nodes are labeled from 0 to Number of nodes - 1.
No two nodes have the same label.
Custom Input:

Input Format:

The first two lines contain the total number of nodes and the label of the root node respectively.
After that, all of the edges are listed as a triplet in separate lines containing the label of the parent node, label of the child node and a character between ‘L’ and ‘R’ depending upon whether we are adding a left child or the right child node to the parent node.
Input for “Example One” above would be:

5

0

0 1 L

0 2 R

1 3 L

1 4 R

Output Format:

The output contains the labels of the nodes in separate lines.
Output for “Example One” above would be:

0

1

3

4

2
'''

#Approach 1

"""
    class TreeNode():
        def __init__(self, label=None, left_ptr=None, right_ptr=None):
            self.label = label
            self.left_ptr = left_ptr
            self.right_ptr = right_ptr

    Complete the function below.
    The function accepts a TREENODE as input
    and is expected to return an INTEGER ARRAY.
"""

def preorder(root):
    if root is None:
        return []
    results = []
    stack = [root]
    while stack:
        node = stack.pop()
        results.append(node.label)
        if node.right_ptr:
            stack.append(node.right_ptr)
        if node.left_ptr:
            stack.append(node.left_ptr)
    return results

#Approach 2

"""
    class TreeNode():
        def __init__(self, label=None, left_ptr=None, right_ptr=None):
            self.label = label
            self.left_ptr = left_ptr
            self.right_ptr = right_ptr

    Complete the function below.
    The function accepts a TREENODE as input
    and is expected to return an INTEGER ARRAY.
"""

def preorder(root):
    results = []
    def preorderhelper(root):
        if root is None:
            return []
        results.append(root.label)
        preorderhelper(root.left_ptr)
        preorderhelper(root.right_ptr)
    preorderhelper(root)
    return results
