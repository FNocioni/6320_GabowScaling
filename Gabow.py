# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 17:31:57 2022

@author: feden
"""

from queue import PriorityQueue
import math

class Graph:
    def __init__(self, n):
        self.v = n
        self.edges = list()
        for i in range(n):
            l = list()
            for j in range(n):
                l.append(-1)
            self.edges.append(l)
        self.visited = []
        
    def add_edge(self, u, v, w):    #'u' -> 'v' with weight 'w'
        self.edges[u][v] = w
        #self.edges[v][u] = w       Uncomment for undirected graphs
        
    def modifyEdge(self, u, v, w):
        self.edges[u][v] = w
        #self.edges[v][u] = w       Uncomment for undirected graphs

def Dijkstra(G, s):
    D = dict()
    Paths = dict()
    for v in range(G.v):
        D[v] = float(math.inf)
        Paths[v] = ""
    
    D[s] = 0
    Paths[s] = str(s)
    P = PriorityQueue()
    P.put((0, s))

    while not P.empty():
        (d, cur) = P.get()
        G.visited.append(cur)

        for neighbor in range(G.v):
            if G.edges[cur][neighbor] != -1:
                distance = G.edges[cur][neighbor]
                
                if neighbor not in G.visited:
                    old_cost = D[neighbor]
                    new_cost = D[cur] + distance
                    
                    if new_cost < old_cost:
                        P.put((new_cost, neighbor))
                        D[neighbor] = new_cost                        
                        Paths[neighbor] = Paths[cur] + "->" + str(neighbor)
                    

    return (D, Paths)


def Gabow(G, s):
    L = 0
    m = 0
    #Fetch maximum weighted edge (-1 means that no edge exists)
    for i in G.edges:
        for j in i:            
            if(j != 1):
                m += 1
            if(L < j and j != -1):
                L = j
            
    R = max(2, m/G.v)
    if(L <= R):
        return Dijkstra(G, s)
    else:
        for i in range(len(G.edges)):
            for j in range(len(G.edges)):
                if(G.edges[i][j] != -1):
                    newWeight = math.floor(G.edges[i][j]/2)
                    G.modifyEdge(i, j, newWeight)
    return Dijkstra(G, s)

def initGraph():
    g = Graph(5)
    g.add_edge(0, 1, 3)
    g.add_edge(0, 2, 2)
    g.add_edge(0, 4, 5)
    g.add_edge(1, 3, 6)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 4, 4)    
    g.add_edge(3, 2, 4)
    g.add_edge(4, 1, 3)
    g.add_edge(4, 3, 2)
    
    return g

g = initGraph()
(D_dijkstra, P_dijkstra) = Dijkstra(g, 0)
 
g = initGraph()
(D, P) = Gabow(g, 0)

for vertex in range(len(D)):
    print("Dijkstra Path:", P_dijkstra[vertex])
    print("Gabow's Path:", P[vertex])    
    print("Actual Distance: ", D_dijkstra[vertex])
    print("Scaled (Gabow Evaluated) Distance: ", D[vertex])   
    print("------------------------------")