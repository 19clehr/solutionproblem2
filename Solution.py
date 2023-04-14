from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys

class Solution:

    def __init__(self, problem, isp, graph, info):
        self.problem = problem
        self.isp = isp
        self.graph = graph
        self.info = info
    
    

    def output_paths(self):

        paths, bandwidths, priorities = {}, {}, {}
        bandwidths.update(self.info["bandwidths"])

        def d(nodeList,parentdict):
            min_weight = -1
            min_node = -1
            min_parent = -1

            for node in nodeList:

                parent = parentdict[node]
                parent_band = self.info["bandwidths"][parent]
                node_band = self.info["bandwidths"][node]

                if (node in self.info["alphas"]):
                    if node_band >= self.info["alphas"][node]:
                        continue 

                if (node_band + parent_band > min_weight):
                    min_node = node
                    min_weight = node_band+parent_band
                    min_parent = parent

            if (min_node == -1):
                    return None
                
            return min_node, min_weight, min_parent
        
        #print(highest_ban_parent_dict)
        #node, node badwidth
        for i in self.info["list_clients"]:
            tovisit = []
            parentdict = {}
            explored_node = [(self.isp,-1)]
            explored = []
            explored.append(self.isp)

            for vertex in self.graph[self.isp]:
              tovisit.append(vertex)
              parentdict[vertex] = self.isp
            
            #explored = node, parent
            currenttovisit = tovisit
            while (i not in explored_node):
                    #print(currenttovisit)
                    #print(explored)
                    node_picked, bandpicked, parent = d(currenttovisit,parentdict)
                    if(node_picked is None):
                        break
                    explored_node.append((node_picked, parent))
                    explored.append(node_picked)
                    for j in self.graph[node_picked]:
                         if j not in currenttovisit:
                              if(j not in explored and j not in explored_node[0]):
                                currenttovisit.append(j)
                                #print('node_picked')
                                print(node_picked)
                               #print(currenttovisit)
                                parentdict[j] = node_picked
                    self.info["bandwidths"][node_picked] = bandpicked
                    currenttovisit.remove(node_picked)
                    #print(currenttovisit)

            paths[i] = [i]
            current = explored_node[-1][0]
            while current != self.isp:
                 paths[i].append(current)
                 current = parentdict[current]
            paths[i].reverse()
            
        #paths = bfs_path(self.graph,self.isp,self.info["list_clients"])
        return (paths, bandwidths, priorities)
