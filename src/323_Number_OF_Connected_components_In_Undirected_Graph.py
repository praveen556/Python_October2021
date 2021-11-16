'''
Given n nodes labeled from 0 to n-1 and a list of undirected edges(Each Edge is a Pair of nodes), Write a function
to find the number of connected componenets in an undirected graph

Input: n=5 edges = [[0,1],[1,2],[3,4]]

Output: 2

Input n =5 edges [[0,1],[1,2],[2,3],[3,4]]

Output = 1
'''
from queue import Empty
from queue import Queue

def connected_components(n, edges):

    adj_edges = [[] for i in range(n)]
    #Building Adjecent list for undirected Graph
    for src,dst in edges:
        adj_edges[src].append(dst)
        adj_edges[dst].append(src)
    #No vertex is visited, so assigning all of them as -1
    visited = [-1]*n

    def bfs(source):
        q = Queue()
        q.put(source)
        visited[source] = 1

        while q:
            node = q.get()
            for neighbors in adj_edges[node]:
                if visited[neighbors] == -1:
                    visited[neighbors] == 1
                    q.put(neighbors)
    connected = 0
    for v in range(n-1):
        if visited[v]==-1:
            connected +=1
            bfs(v)
    return connected
connected_components(5, [[0,1],[1,2],[2,3],[3,4]])
