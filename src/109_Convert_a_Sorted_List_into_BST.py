'''
Given a singly linked list with elements sorted in ascending order, your task is to convert it into a height-balanced binary search tree.

Example One:

Input:



Output:



Example Two:

Input:



Output:



Notes:

A binary tree is called height-balanced if for any node, the difference in the heights of its left and right subtree does not exceed by one.
The input list does not contain nodes with duplicate values.
Constraints:

1 <= Length of the Linked List <= 20000.
-109 <= Value of a Node <= 109.
Custom Input:

Input Format:

The first line of input contains the number of nodes in the singly linked list.
The values of the nodes are then listed, one in each line.
Input for “Example One” above would be:

7

-1

2

3

5

6

7

10

Output Format:

The output contains the inorder traversal of the values of the returned binary search tree with each value printed in a separate line.
Output for “Example One” above would be:

-1

2

3

5

6

7

10
'''



"""
    For your reference:
    class SinglyLinkedListNode:
        def __init__(self, node_data):
            self.data = node_data
            self.next = None

    class TreeNode():
        def __init__(self, val=None, left_ptr=None, right_ptr=None):
            self.val = val
            self.left_ptr = left_ptr
            self.right_ptr = right_ptr

    Complete the function below.
"""

def sorted_list_to_bst(head):
    """
        Args:
         head(SinglyLinkedListNode_int32)
        Returns:
         TreeNode_in32


    """
    arr = []
    arr.append(head.data)
    while head.next is not None:
        head = head.next
        arr.append(head.data)

    def make_bst_helper(arr, start, end):
        if start > end:
            return
        mid = start + (end-start)//2
        root = TreeNode(arr[mid])
        if start == end:
            return root
        else:
            root.left_ptr=make_bst_helper(arr, start, mid-1)
            root.right_ptr=make_bst_helper(arr,mid+1, end)
            return root

    return make_bst_helper(arr, 0, len(arr)-1)
