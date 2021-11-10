'''
Nary Tree Level Order Traversal

Given an n-ary tree, list the labels of the nodes, level by level from left to right.

Example One:

Input:



Output: [ [ 1 ],

	       [ 3, 4, 2 ],

               [ 5, 6 ] ]

Example Two:

Input:



Output: [ [ 1 ],

               [ 2 ],

               [ 4 ],

               [ 3 ] ]

Notes:

Constraints:

1 <= Number of Nodes <= 20000.
1 <= Node Labels <= Number of Nodes.
No two nodes in the tree have the same label.
The node with label 1 will always be the root node.
Custom Input:

Input Format:

The first line contains the number of edges.
In the next “number of edges” number of lines, the i-th line contains the label of the parent node of the i-th edge present in the tree.
The next line contains the number of edges.
In the next “number of edges” number of lines, the i-th line contains the label of the child node of the i-th edge present in the tree.
(Note: For any parent node, the edges are given from left to right).

Input for “Example One” above would be:

5

1

1

1

4

4

5

3

4

2

5

6

Output Format:

Labels of the nodes from different levels starting from the top to the bottom should be listed in separate lines.
The node labels within a level should be separated by spaces.
Output for “Example One” above would be:

1

3 4 2

5 6
'''
'''
    class TreeNode:
        def __init__(self, _label):
            self.label = _label
            self.children = []

    Complete the function below.
    The function accepts a TREENODE as input
    and is expected to return a TWO-DIMENSIONAL LIST OF INTEGERS.
'''

#Appraoch 1
def level_order(root):
    if root is None:
        return []
    results = []
    stack = [root]
    while stack:
        temp = []
        count = len(stack)
        while count > 0:
            node = stack.pop(0)
            for i in node.children:
                stack.append(i)
            temp.append(node.label)
            count -= 1
        results.append(temp)
    return results
