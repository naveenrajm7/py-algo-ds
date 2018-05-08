#! /usr/bin/python3
from collections import defaultdict


class Graph:

    def __init__(self):
        ''' using default dict to store edges & weights of initialized graph '''
        self.graph = defaultdict(dict)

    def addEdge(self, u, v, weight=1):
        ''' adding edges u->v with weight or 1 otherwise '''
        self.graph[u][v] = weight

    def dijkstra(self, src):
        ''' to find all pair shortest path - minimum spanning tree for the given node'''
        spanning_tree = {}
        permanent_list = spanning_tree
        tentitive_list = {} # to store node and value to reach it
        visited = [False]*(len(self.graph)) # to keep track of visted vertices
        # add source to tentative list
        tentitive_list[src] = 0
        # run till tentative list is empty
        while tentitive_list:
            # can use prority queue here
            tentitive_minimum = min(tentitive_list,key=tentitive_list.get) #move minimum of tentative to permanent_list
            permanent_list[tentitive_minimum] = tentitive_list.get(tentitive_minimum)
            visited[tentitive_minimum] = True
            # add all unvisited neighbouring nodes of last added node(to permanent_list) to tentitive list
            for neighbour in self.graph[tentitive_minimum]:
                if not visited[neighbour]:
                    new_dist = tentitive_list[tentitive_minimum] + self.graph[tentitive_minimum][neighbour]
                    # if new cost is less than cumulative cost of node in tentitive list replace it.
                    if new_dist < tentitive_list.get(neighbour, float('inf')):
                        tentitive_list[neighbour] = new_dist

            del tentitive_list[tentitive_minimum]

        return spanning_tree

if __name__ == "__main__":

    q = int(input("Enter number of graphs\n"))
    for a0 in range(q):
        g = Graph()
        print("Enter no. of vertices and edges")
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]

        print("Enter %d edges u->v:w\n"%m) # directed graph ,add two edges for undirected
        for edges_i in range(m):
            u,v,w = [int(edges_temp) for edges_temp in input().strip().split(' ')]
            g.addEdge(u,v,w)
            g.addEdge(v,u,w)

        print("Enter edge 0-(%d) to start traversal"%(n-1))
        source = int(input().strip())

        all_pair_shortest_path = g.dijkstra(source)
        print(all_pair_shortest_path)
