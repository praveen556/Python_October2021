class TreeNode:
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr


def verticalsum(TreeNone root):

    result  = []
    self.col_map = collections.defaultdict(lambda: [])
    self.min_col, self.max_cal = 0, 0
    self.traverse(root, 0, 0)

    for col in range(self.min_col, self.max_col+1):
        if col in self.col_map:
            #put values from loweer rows first, If rows are same order by val
            #self.col_map[col].sort(key=lambda x: (x[0],x[1]))
            col_sum = 0
            for _,val in self.col_map[col]:
                col_sum += val
            result.append(col_sum)
    return result



def traverse(self, node, row, col):
    if node:
        self.col_map[col].append(row, node.val)
        self.min_col = min(self.min_col, col)
        self.max_val = max(self.max_col, col)
        self.traverse(self, node.left, row+1, col-1)
        self.traverse(self, node.right, row+1, col+1)
