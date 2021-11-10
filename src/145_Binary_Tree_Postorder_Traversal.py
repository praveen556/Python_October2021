
"""
Given a binary tree, find the postorder traversal of its nodes’ labels.

Example One

Input:



Output: [ 3, 4, 1, 2, 0 ]

Example Two:

Input:



Output: [ 3, 2, 1, 0 ]

Notes:

The postorder traversal visits all the nodes of a binary tree by recursively visiting the left subtree, then the right subtree and finally visiting the root.

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

3

4

1

2

0



    class TreeNode():
        def __init__(self, label=None, left_ptr=None, right_ptr=None):
            self.label = label
            self.left_ptr = left_ptr
            self.right_ptr = right_ptr

    Complete the function below.
    The function accepts a TREENODE as input
    and is expected to return an INTEGER ARRAY.
"""

def postorder(root):
    if not root:
        return []
    results = []
    stake = [root]
    while stake:
        node = stake.pop()
        results.append(node.label)
        if node.left_ptr:
            stake.append(node.left_ptr)
        if node.right_ptr:
            stake.append(node.right_ptr)
    return results[::-1]

'''Approach 2'''

def postorder(root):
    if not root:
        return []
    results = []
    def postorderHelper(root):
        if root is None:
            return
        postorderHelper(root.left_ptr)
        postorderHelper(root.right_ptr)
        results.append(root.label)
    postorderHelper(root)
    return results
