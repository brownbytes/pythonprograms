'''
###########
name:durga
program : Depth First Search Algorithm for topological ordering

DepthFirst Search involves passing deeper into the graph with each step
unlike Breadth First Search which passes each layer systematically.
Depth first search is stach based so a simple Python List can be used.
Recurision intrinsically implements stacks 

few stack functions: LIFO
L = [] assigns list
L.pop() pop out the last inputted element
L.append() add an element to the stach


labels : when DFS_loop runs on Gr(test2), the output is 1,2,4,5,7,8,9 , 3 and 6 are eliminated
'''

import sys
import resource
import time
import cProfile
sys.setrecursionlimit(2**20)
resource.setrlimit(resource.RLIMIT_STACK, (2**25,2**25))

# reading input graph file
''' first element in list is a node initialise a node'''


G = {}
Gr = {}
discovered = {} # notes if the node has been discovered
finish_time = 0 #
cur_source = None #keeps track of source vertex-leaders
leader = {} # to track leaders to the nodes
rev = True
fin_list = []
temp_fin_list = {}
N = 875714
#N = 50
t0 = time.clock()
#framing the input graph
##
for i in range(1,N+1):
    G[i] = []
    Gr[i] = []
    fin_list.append(i)
    discovered[i]=False
    leader[i] = []

with open('SCC.txt') as fd:
    for line in fd:  # this way of reading file takes appr. 22sec
        nodelist = line.split()
        G[int(nodelist[0])].append(int(nodelist[1]))
        Gr[int(nodelist[1])].append(int(nodelist[0]))

# DFS
def DFS(graph,node):
    global discovered
    global leader
    global finish_time
    global fin_list

    discovered[node]=True # source has been discovered

    if not(rev): #calculating list of nodes with same leader
        leader[cur_source].append(node)

    for nei in graph[node]:# selecting a single neighbour of node
        if discovered[nei] == False:
            DFS(graph,nei)
                
    if rev:       
        finish_time += 1
        fin_list[finish_time-1] = node

def DFS_loop(graph): 
    global discovered #nodes as they get discovered
    global cur_source # keeps track of current node whose finish time has to be yet calculated
    global rev # stores if reverse graph or normal graph is being considered

    ft  = fin_list[::-1]

    for i in ft:#running DFS on each and every key in graph, children will be computed by dfs [9,8,7,6,5,4,3,2,1]
        if discovered[i]==False:
            cur_source = i
            DFS(graph,i)

    rev = False


#traverse the reverse Gr to discover
def kosaraju_main():

    DFS_loop(Gr)    

    for i in range(1,N+1):
        discovered[i]=False
            
    DFS_loop(G)
   
    first = 0
    second = 0
    third = 0
    fourth = 0
    fifth = 0

    for aleader in leader.keys():
        if len(leader[aleader]) > fifth:
            if len(leader[aleader]) > fourth:
                if len(leader[aleader]) > third:
                    if len(leader[aleader]) > second:
                        if len(leader[aleader]) > first:
                            fifth = fourth
                            fourth = third
                            third = second
                            second = first
                            first = len(leader[aleader])
                        else:
                            fifth = fourth
                            fourth = third
                            third = second
                            second = len(leader[aleader])
                    else:
                        fifth = fourth
                        fourth = third
                        third = len(leader[aleader])
                else:
                    fifth = fourth
                    fourth = len(leader[aleader])
            else:
                fifth = len(leader[aleader])
                            
    
    print first,second,third,fourth,fifth
        
if __name__ == '__main__':
    kosaraju_main()
    #cProfile.run('kosaraju_main()','kosaraju.profile')
    
#use unit tests

    
