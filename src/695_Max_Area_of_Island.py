'''
Search For The Largest Island

Given a two-dimensional array containing 0s and 1s, find the size of the largest island. If there is no island return 0.

An island is a group of 1s connected vertically or horizontally.

Example One

Input: grid = [

	[1, 1, 0],

	[1, 1, 0],

	[0, 0, 1],

]

Output: 4

There are two islands:

1) [(0, 0), (0, 1), (1, 0), (1, 1)]

2) [(2, 2)]

The size of the largest island is 4.

Example Two

Input: grid = [

	[0, 0, 0],

	[0, 0, 0],

	[0, 0, 0],

]

Output: 0

Notes

Constraints:

1 <= number of rows <= 200
1 <= number of columns <= 200
Custom Input

Input Format:

First line contains an integer R denoting the number of rows.

Second line contains an integer C denoting the number of columns.

Next R lines will contain C space separated integers each. Integers will be either 0 or 1. Input from “Example One” above would look like this:

3

3

1 1 0

1 1 0

0 0 1

Output Format:

Single line with an integer on it. Output from “Example One” above would look like this:

4
'''



from collections import deque

def max_island_size(grid):
    """
    Args:
        grid (List[List[int]])
    Returns:
        int
    """
    # Write your code here
    rows = len(grid)
    cols = len(grid[0])

    #Buliding Visited List
    island_size = 0

    visited = [[-1 for i in range(cols)] for j in range(rows)]

    def get_neighbors(i,j):

        neighbors = []

        #Up
        if i >0 and grid[i-1][j]==1:
            neighbors.append((i-1,j))

        #Down
        if i < rows-1 and grid[i+1][j]==1:
            neighbors.append((i+1,j))

         #Left
        if j >0 and grid[i][j-1]==1:
            neighbors.append((i,j-1))

        #Right
        if j <cols-1 and grid[i][j+1]==1:
            neighbors.append((i,j+1))

        return neighbors


    def bfs(i,j):
        q = deque([(i,j)])

        visited[i][j] = 1
        islands = 1

        while q:
            c_i, c_j = q.popleft()

            neighbors = get_neighbors(c_i, c_j)

            for n_i,n_j in neighbors:
                if visited[n_i][n_j] == -1:
                    visited[n_i][n_j] =1
                    q.append([n_i,n_j])
                    islands+= 1

        return islands




    for i in range(rows):
        for j in range(cols):
            if visited[i][j]==-1 and grid[i][j]==1:
                temp = bfs(i,j)

                island_size = max(island_size, temp)

    return island_size
