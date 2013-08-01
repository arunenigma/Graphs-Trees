# Graph Traversal using DFS and BFS Algorithms
# based on Guido Van Rossum's example script

from pprint import pprint
import numpy as np
from numpy.random import RandomState

class ShortestPath(object):
    def __init__(self):
        """
            Constructor
        """
        pass
        
    def createGraph(self):
        """
            W -> Adjacency Matrix
            For test cases, this method is modified to generate random 
            weight matrix with zero weights for no edges.
            
               Graph is undirected with only positive weights 
               
            @prng: pseudo random number generator
        """
        '''
        _ = 0  # no edge
            # a  b  c  d
        W = [[_, 1, 3, 4],  # a
             [1, _, 2, 1],  # b
             [_, 1, _, 1],  # c
             [5, 1, 2, _]]  # d
        #print W
        '''
        prng = RandomState()  # alternative to random.seed
        w = prng.randint(0, 6, size=16)
        # inflating 1D array to 2D square matrix
        W = w.reshape(4, 4)
        #pprint(W)
        #print W[a][d]
        W = np.array(W) 
        W_symm = (W + W.T)/2  # making the matrix symmetric
        np.fill_diagonal(W_symm, 0)
        return W_symm
        
    def graphToDict(self, G):
        G_dict = {}
        nodes = ['A', 'B', 'C', 'D']
        
        for i in range(4):
            neighbors = []
            for j in range(4):
                if not G[i][j] == 0:
                    neighbors += [nodes[j]]
            G_dict[nodes[i]] = neighbors 
        #print G_dict
        return G_dict
           
    def recursiveDFS(self, G, s, path):
        """
            @param G: graph as a dict
            @param s: start node
            @param path: DFS traversal path
        """
        path = path + [s]  
        for node in G[s]:
            if not node in path:
                path = self.recursiveDFS(G, node, path)
        return path
            
        
    def recursiveBFS(self, G, s, path):
        pass
        
    def iterativeDFS(self, G, s, path):
        q = [s]  # q -> queue
        while q:  # implying q not empty
            v = q.pop(0) 
            if v not in path:
                path = path + [v]
                q = G[v] + q
        return path
        
    def iterativeBFS(self, G, s, path):
        q = [s]  # q -> queue
        while q:  # implying q not empty
            v = q.pop(0) 
            if v not in path:
                path = path + [v]
                q = q + G[v]
        return path
                        
sp = ShortestPath()
G = sp.graphToDict(sp.createGraph())
print G
print sp.recursiveDFS(G, 'C', path=[])
#sp.recursiveBFS(G, 'C', p=[])
print sp.iterativeDFS(G, 'C', path=[])
print sp.iterativeBFS(G, 'C', path=[])
       
