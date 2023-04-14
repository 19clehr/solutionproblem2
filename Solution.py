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

        def d(self,nodeList,parentdict):
            min = -1
            min_node = -1
            min_parent = -1
            for node in nodeList:
                parent = parentdict(node)
                parent_band = self.info["bandwidths"][parent]
                node_band = self.info["bandwidths"][node]
                if node_band+parent_band > min:
                    min_node = node
                    min = node_band+parent_band
                    min_parent = parent

            return min_node, min, min_parent
        """
        This method must be filled in by you. You may add other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        """
        paths, bandwidths, priorities = {}, {}, {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN

        #print(highest_ban_parent_dict)
        tovisit = []
        initparentdict = {}
        for i in self.graph[self.isp]:
              tovisit.append(i)
              parentdict[i] = self.isp
              #node, node badwidth
        for i in self.info["list_clients"]:
            explored = [self.isp,-1]
            
            parentdict = initparentdict
            #explored = node, parent
            currenttovisit = tovisit
            while i not in explored:
                    node_picked, bandpicked, parent = d(currenttovisit,parentdict)
                    explored.append[node_picked,parent]
                    for j in self.graph[node_picked]:
                         if j not in tovisit:
                              tovisit.append(j)
                              parentdict[j] = node_picked
                    self.info["bandwidths"][node_picked] = bandpicked

            paths[i] = [i]
            current = explored[-1][1]
            while current != self.isp:
                 paths[i].append(current)
                 current = parentdict[current]
        #paths = bfs_path(self.graph,self.isp,self.info["list_clients"])
        return (paths, bandwidths, priorities)

    
        
