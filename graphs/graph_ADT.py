#Graph() creates a new, empty graph.
#addVertex(vert) adds an instance of Vertex to the graph.
#addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
#addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
#getVertex(vertKey) finds the vertex in the graph named vertKey.
#getVertices() returns the list of all vertices in the graph.
#in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    #user added
    def printNone(self):
        print("nothing")

    #user added
    def printVertices(self):
        """Graph -> string 
        iterates through all vertices in vertlist and prints, also prints numVertices"""
        print("numvertices: {}".format(self.numVertices))
        print("all vertices: {}".format(self.vertList.keys()))
        #for n in self.vertList:
        #    print(n)
        print("printing all of getConnections now")
        for v in g:
            for w in v.getConnections():
                print("({0}, {1})".format(v.getId(), w.getId()))

    #user added
    def printNeighbors(self):
        for v in g:
            for nbr in v.connectedTo:
                print(nbr)

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def getConnectionPairs(self):
        for v in g:
            for w in v.getConnections():
                print("({0}, {1})".format(v.getId(), w.getId()))


#simple test print out
g = Graph()
for i in range(6):
	g.addVertex(i)
g.vertList

#word ladder problem
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

#traverse(g.getVertex('sage'))
g = Graph()
g.addVertex(10)
print(g.vertList)

for i in range(6):
    g.addVertex(i)
print(g.vertList)

g.addEdge(0,1,5)
g.addEdge(0,3,8)
g.addEdge(1,12,9)
g.addEdge(1,1,9)
g.addEdge(2,3,7)
g.addEdge(2,4,8)
g.addEdge(3,8,6)
g.addEdge(3,5,6)
g.addEdge(4,2,1)
g.addEdge(5,2,5)



g.printVertices()
g.getVertices()
g.printNone()
#g.getConnectionPairs()

for v in g:
    for w in v.getConnections():
        print("({0}, {1})".format(v.getId(), w.getId()))

print("print neighbors")
print(g.printNeighbors())