'''
name:durga
program : graph contraction algorithm

the algorithm involves smashing 2 nodes into a super node by removing a single edge
and associate the remaining edges to the new super node

'''

import random
import copy


'''when graph is left with only 2 nodes ,ie supernodes , the program can stop running
edgenode is a dictionary which will map each node to its corresponding edges and be updated upon contraction'''

edgevertex = {}

fd = open('graph.txt','r')

''' below peice of code formats the file into a edgevertex[vertex]=[list od edges] dict'''

while True:
    tempvertex = fd.readline().split()
    tempedge = [] #holds edges for each vertex
    if not tempvertex:
        break
    else:
        vertex = int(tempvertex[0])
        for v in tempvertex[1:]: #not to include self vertex
            edge = [vertex,int(v)]
            tempedge.append(edge)
    edgevertex[vertex] = tempedge # returns a map with vertices and corresponding edges
    edge=[]

def graphadj(edgevertex):

    while len(edgevertex.keys()) > 2:
        #choosing a random edge
        randomedge = random.choice(random.choice(edgevertex.values()))
        supernode = randomedge[0]
        mergenode = randomedge[1] # to be contracted
        
        #moving all the edges corresponding to mergenode to supernode and deleting traces of mergenode
        edgevertex[supernode].extend(edgevertex[mergenode]) # add them to the supernode

        # remove all occurences
        while edgevertex[supernode].count(randomedge) > 0: # very important, else only the first occurence is removed , giving  2 hr heartache
            if randomedge in edgevertex[supernode]: #removing the edge from supernode list
                edgevertex[supernode].remove(randomedge)   
        while edgevertex[supernode].count([randomedge[1],randomedge[0]]) > 0:
            if [randomedge[1],randomedge[0]] in edgevertex[supernode]:
                edgevertex[supernode].remove([randomedge[1],randomedge[0]])

        for e in edgevertex[supernode]: #changing all mergenodes to supernodes in supernode
            for n,i in enumerate(e):
                if i == mergenode:
                    e[n] = supernode

            if e == [supernode,supernode]:
                edgevertex[supernode].remove(e)
                
        del(edgevertex[mergenode]) #deleting traces of mergenode
            
        for vrtx in edgevertex.keys():#altering the rest of the dictionary to substitute mergernode with supernode
            for eachedge in edgevertex[vrtx]: #using enumerator to replace mergenode with supernodes
                for n,i in enumerate(eachedge):
                    if i == mergenode:
                        eachedge[n] = supernode

            if vrtx == supernode and edgevertex[vrtx].count([supernode,supernode])>0:
                while edgevertex[vrtx].count([supernode,supernode]) > 0:
                    edgevertex[vrtx].remove([supernode,supernode])

    return min(len(edgevertex[edgevertex.keys()[0]]),len(edgevertex[edgevertex.keys()[1]]))

mini = 1000
i= 0
while i <50:
    edgevertex1 = copy.deepcopy(edgevertex)
    num = graphadj(edgevertex1)
    if num < mini:
        mini = num
    i += 1

print mini

    

    
