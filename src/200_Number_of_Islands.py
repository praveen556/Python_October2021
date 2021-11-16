'''

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''



#
#Complete the function count_islands
#The function takes integers 2D integer array, matrix, as parameter.
#
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        islands = 0

        def get_neighbors(i, j):

            neighbors = []

    #UP
            if i > 0 and grid[i-1][j]=="1":
                neighbors.append((i-1, j))

    #Left
            if j >0 and grid[i][j-1]=="1":
                neighbors.append((i,j-1))

    #Down
            if i < rows-1 and grid[i+1][j]=="1":
                neighbors.append((i+1, j))

    #Right
            if j < cols-1 and grid[i][j+1]=="1":
                neighbors.append((i,j+1))

            return neighbors

        def bfs(i,j):
            q = deque([(i,j)])

            visited[i][j] = True

            while q:
                c_i, c_j = q.popleft()

                neighbors = get_neighbors(c_i, c_j)

                for n_i,n_j in neighbors:
                    if not visited[n_i][n_j]:
                        q.append([n_i,n_j])
                        visited[n_i][n_j] = True
            return


        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j]=="1":
                    bfs(i,j)
                    islands += 1
        return islands



        
