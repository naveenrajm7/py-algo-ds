#! /usr/bin/python3
from collections import defaultdict
''' Breadth First Search : finding Path with fewest number of edges
Traversal and finding minimum edges(weigth)
Data Structure used : queue

Deapth First search
data struture used : stack (automatic recusrive calls)
All graph problems be solved using adjacency lists which has complexity O(|V|+|E|) ,  [ adjacency matrix has O(|v|2) ] '''

class Graph:

    def __init__(self):
        ''' using default dict to store edges & weights of initialized graph '''
        self.graph = defaultdict(dict)

    def addEdge(self, u, v, weight=1):
        ''' adding edges u->v with weight or 1 otherwise '''
        self.graph[u][v] = weight

    def bfs(self, vertex, edges, s):
        ''' bfs traversal from vertex s '''
        visited = [False]*(vertex)  # to keep track of visted vertices
        distance = []*(vertex)  # distance of all vertices from s
        queue = []  # data structure to hold visted vertex in FIFO fashion & acheive BFS
        traverse = [] # to track the order of visit

        queue.append(s)
        visited[s] = True

        while queue:

            s = queue.pop(0)
            traverse.append(s)

            for vertices in self.graph[s]:
                if not visited[vertices]:
                    #distance[vertices] = self.graph[s][vertices] + distance[s] #to find minimum edges(weight)
                    queue.append(vertices)
                    visited[vertices]=True

        return traverse

    def dfs(self, visited_dfs, traverse, s):
        '''dfs traversal from vertex s recursively'''
        visited_dfs[s] = True
        traverse.append(s)
        for vertices in self.graph[s]:
            if not visited_dfs[vertices]:
                self.dfs(visited_dfs, traverse, vertices)
        return traverse

if __name__ == "__main__":

    q = int(input("Enter number of graphs\n"))
    for a0 in range(q):
        g = Graph()
        print("Enter no. of vertices and edges")
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]

        print("Enter %d edges u->v:w\n"%m) # directed graph ,add two edges for undirected
        for edges_i in range(m):
            u,v = [int(edges_temp) for edges_temp in input().strip().split(' ')]
            g.addEdge(u,v)
            g.addEdge(v,u)

        choice = int(input("enter 1 for BFS other no. for DFS\n"))
        print("Enter edge 0-(%d) to start traversal"%(n-1))
        s = int(input().strip())

        if choice == 1:
            print(g.bfs(n, m, s))
        else:# dfs
            visited_dfs = [False]*n
            traverse_dfs = []
            print(g.dfs(visited_dfs, traverse_dfs, s))
