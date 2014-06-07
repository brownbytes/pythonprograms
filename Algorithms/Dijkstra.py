'''
###########
name:durga
program : dijkstra's Shortest path algorithm


psuedocode:
dist[s] <-- 0 (ditance to source vertex is zero)
for all v in V-{s}
    do dist[v] <-- highest number (set all other distances to infinity)
S <-- empty (S , the set of visited vertices is initially empty)
Q <-- V (Q, the queue initially contains all the vertices)
while Q is not empty:
    do u <-- mindistance(Q,dist) (select the element of Q with min.distance)
        S <--SU{u} (add u to the list of visited vertices)
        for all v E neighbours[u]
            do if dist[v] > dist[u] + w(u,v) (if new shortest path found)
                then d[v] <-- d[u] + w(u,v)  (set new value f shortest path)

    return dist (return traceback code)
'''

#from heapq import heappush,heappop # priority queu
import Queue

# reading input graph file
''' first element in list is a node initialise a node'''

H = [[0,1000000]] # can be heapified later heapq.heapify(x)
N = 200

dist = [0] # dist[node] = path lenght from source, first element is the source

G = {} #{s :{v1:l1,v2:l2,v3:l3}......}
Gall = {} # { s:[v1,l1],....} all vertices unreachable longest distance
vertices = [] #all vertices
nei = {} # set of nei for a vertex
source = 1
#S = [] # set of visited vertices , initally empty

#input graph

for i in range(1,N+1):
#for i in range(0,N):
    G[i] = {} 
    nei[i] = []
    vertices.append(i)
    dist.append(1000000) #setting all distance to all nodes as max

with open('dijkstraData.txt') as fd:
    for line in fd:

        nodelist = line.split()
        for i in range(1,len(nodelist)):           
            node = nodelist[i].split(',')            
            G[int(nodelist[0])][int(node[0])]=int(node[1])
            nei[int(nodelist[0])].append(int(node[0]))


def mindistance(Q,dist):

    mini = 1000000
    tempdist= []
    
    for node in Q: # dist of all vertices in Q to source
        if node in nei[source]: # if a immediate nei of source               
            if G[source][node] < dist[node]: #setting up distances from source to all vertices
                dist[node] = G[source][node]

    for i in Q:
        tempdist.append(dist[i])

    mini = min(tempdist)
##         if dist[i] < mini:
##            mini = dist[i]

    for i in Q:
        if dist[i] == mini:
            return i #return node of closest distance
    
              
#finding shortest path between source and all nodes
def dijkstra(graph,source):

    global dist
    
    S=[source]# set of visited vertices , initally empty

    dist[source] = 0 #setting source distance to 0

    Q = [] # queue of remaining vertices
    for ver in vertices:
        if ver != source: Q.append(ver) # putting all vertices in a queue
    
    while len(Q) != 0: #while all vertices are not visited
        
        edge = mindistance(Q,dist) # return the nearest neighbour of source

        if edge not in S: S.append(edge) # add the node in discovered

        for v in nei[edge]: #for each edge this nei calculate cost
            if v not in S:
                if dist[v] > dist[edge] + G[edge][v]:
                    dist[v] = dist[edge]+G[edge][v]
        #source = edge
        Q.remove(edge)


    return dist

distances = dijkstra(G,source)

itemlist = [1,2,3] #  destination list

for a in itemlist:
    print a,distances[a]


