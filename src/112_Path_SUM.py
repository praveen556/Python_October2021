'''

'''


'''
    class TreeNode():
        def __init__(self, val=None, left_ptr=None, right_ptr=None):
            self.val = val
            self.left_ptr = left_ptr
            self.right_ptr = right_ptr

    Complete the function below.
    The function accepts a TREENODE and an INTEGER as inputs
    and is expected to return a BOOLEAN.
'''


#Appraoch 1

def path_sum(root, k):
    if root is None:
        return False
    stack = [(root, root.val)]

    while stack:
        node, total = stack.pop()

        if node.left_ptr is None and node.right_ptr is None:
            if total == k:
                return True

        if node.left_ptr:
            stack.append((node.left_ptr, total + node.left_ptr.val))

        if node.right_ptr:
            stack.append((node.right_ptr, total + node.right_ptr.val))
    return False


#Appraoch 2

def path_sum(root, k):
    if not root:
        return False
    if(not root.left_ptr and  not root.right_ptr):
        if k == root.val:
            return True
    return path_sum(root.left_ptr,k-root.val) or path_sum(root.right_ptr,k-root.val)
