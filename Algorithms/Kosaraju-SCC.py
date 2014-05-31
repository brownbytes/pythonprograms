'''
###########
name:durga
program : Depth First Search Algorithm

DepthFirst Search involves passing deeper into the graph with each step
unlike Breadth First Search which passes each layer systematically.
Depth first search is stach based so a simple Python List can be used.Recurision intrinsically implements stacks 



few stack functions: LIFO
L = [] assigns list
L.pop() pop out the last inputted element
L.append() add an element to the stach


labels : when DFS_loop runs on Gr(test2), the output is 1,2,4,5,7,8,9 , 3 and 6 are eliminated
'''
import random

import sys
sys.setrecursionlimit(1000000)

# reading input graph file
''' first element in list is a node initialise a node'''

S = [] # initialising a stack to push navigated vertices in the stack
G = {}
Gr = {}
neighbours = []
discovered =[]# notes if the node has been discovered
finish_time = 0 #
cur_source = None #keeps track of source vertex-leaders
leader = {} # to track leaders to the nodes
rev = True
fin_list = []
j =0

#framing the input graph
fd = open('SCC.txt','r')

while True: #making a graph
    nodelist = fd.readline().split()
    #print nodelist[0]
    if not nodelist:
        break
    else:
        neighbours = []
        rneighbours = []
        #create forward graph
        vertex = int(nodelist[0])            
        neighbours.append(int(nodelist[1]))
        if vertex not in G.keys():
            G[vertex] = neighbours
        elif vertex in G.keys():
            G[vertex].extend(neighbours)

        # reverse graph
            
        rvertex = int(nodelist[1])
        rneighbours.append(int(nodelist[0]))
        if rvertex not in Gr.keys():
            Gr[rvertex] = rneighbours
        elif vertex in G.keys():
            Gr[rvertex].extend(rneighbours)
    print "making graph..." + str(nodelist)
          

# DFS
def DFS(graph,node):
    global discovered
    global S
    global leader
    global finish_time
    global fin_list
    global j # for print only

    follower =[]
    print 'discovering' + str(node)
    discovered.append(node) # source has been discovered
    j += 1
    if not(rev): #calculating list of nodes with same leader
        #leader[node] = cur_source
        follower.append(node)
        if cur_source in leader.keys():
            leader[cur_source].extend(follower)
        elif cur_source not in leader.keys():
            leader[cur_source] = follower

    if node in graph.keys():
        for nei in graph[node]:# selecting a single neighbour of node
            if nei not in discovered:
                DFS(graph,nei)
                
    if rev:       
        finish_time += 1
        #S[finish_time]=node #S[n] = finish_time
        fin_list.append(finish_time)
            

def DFS_loop(graph): #outcall for any dangling nodes which might not fall into the loop ex :test2 # for reverse graph
    global discovered
    global cur_source # keeps track of current node whose finish time has to be yet calculated
    global i
    global rev

    discovered = []
    
    if rev: ft = range(875714,0,-1) # for reverse graph - 1st run of DFS-loop

    else: ft = fin_list[::-1]
        
    for i in ft:#running DFS on each and every key in graph, children will be computed by dfs [9,8,7,6,5,4,3,2,1]
        if i not in discovered:
            cur_source = i
            DFS(graph,i)

    rev = False


#traverse the reverse Gr to discover
def kosaraju_main():
    DFS_loop(Gr)

    DFS_loop(G)

    first = 0
    second = 0
    third = 0
    fourth = 0
    fifth = 0
    #calculating the size of SCC
    for aleader in leader.keys():
        if len(leader[aleader]) > first:
            fifth = fourth
            fourth = third
            third = second
            second = first
            first = len(leader[aleader])
        elif len(leader[aleader]) > second:
            fifth = fourth
            fourth = third
            third = second
            second = len(leader[aleader])
        elif len(leader[aleader]) > third:
            fifth = fourth
            fourth = third
            third = len(leader[aleader])
        elif len(leader[aleader]) > fourth:
            fifth = fourth
            fourth = len(leader[aleader])
        elif len(leader[aleader]) > fifth:
            fifth = len(leader[aleader])

    
    print first,second,third,fourth,fifth
        

kosaraju_main()
#use unit tests
#test5 Answer: 3,2,2,2,1   the 6th value is also a 1, 7th is 0    n =11
#test6 Answer: 6,1,1,0,0
#test7 Answer: 6,3,2,1,0   n = 12
#test8 Answer: 35,7,1,1,1,1,1,1,1,1 n 50
    
