# LAB 08

def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    return(G)



def addEdges(G,edges,directed):
    for i in edges:
        start = i[0]
        end = i[1]
        weight = i[2]
        v = (end, weight)
        value = G[start]
        value.append(v)
        G[start] = value
        if directed == False:
            vv = (start, weight)
            vvalue = G[end]
            vvalue.append(vv)
            G[end] = vvalue
    return(G)

def listOfNodes(G):
    lst = []
    for i in G:
        lst.append(i)
    return(lst)


def listOfEdges(G,directed):
    lst = []
    for i in G:
        value = G[i]
        for j in value:
            tup = (i,j[0],j[-1])
            lst.append(tup)
    if directed == True:
        return(lst)
    
    if directed == False:
        lstt = []
        for i in lst:
            a = i[0]
            b = i[1]
            c = i[-1]
            tup = (b,a,c)
            if tup not in lstt:
                lstt.append(i)
        return(lstt)
            
            
def printIn_OutDegree(G):
    lst = []
    lstt = []
    for i in G:
        lst.append(i)
    string = ''
    for j in lst:
        count = 0
        for k in G:
            for h in G[k]:
                if h[0] == j:
                    count = count +1
        string = string + str(j)+' => In-Degree: '+str(count)+', Out-Degree: '+str(len(G[j]))+'\n'
    return(string)


def printDegree(G):
    string = ''
    for i in G:
        
        a = len(G[i])
        string = string + str(i)+' => '+str(a) + '\n'
    return(string)

def getNeighbors(G,node):
    lst =[]
    for i in G[node]:
        lst.append(i[0])
    return(lst)

def getInNeighbors(G, node):
    lst = []
    for i in G:
        for j in G[i]:
            if j[0] == node:
                lst.append(i)
    return(lst)

def getOutNeighbors(G, node):
    lst = []
    for j in G[node]:
        lst.append(j[0])
    return(lst)

def getNearestNeighbor(G, node):
    value = G[node]
    minimum = (value[0][0],value[0][-1])
    for i in G[node]:
        if i[-1] < minimum[-1]:
            minimum = (i[0],i[-1])
    return(minimum[0])
        

def isNeighbor(G, Node1, Node2):
    for i in G[Node1]:
        if i[0] == Node2:
            return(True)
        
    return(False)


def removeNode(G, node):
    del(G[node])
    for i in G:
        value = G[i]
        for j in value:
            if j[0] == node:
                a = (value.index(j))
                del(value[a])

                
def removeNodes(G, nodes):
    for n in nodes:
        del(G[n])
        for i in G:
            value = G[i]
            for j in value:
                if j[0] == n:
                    a = (value.index(j))
                    del(value[a])

    
def displayGraph(G):
    return(G)


def display_adj_matrix(G):
    a = len(G)
    lstt = []
    for i in range(a):
        lst = []
        ls = [0] * (a)
        lstt.append(ls)
    for j in G:
        value = G[j]
        for k in value:
            aa = k[0]
            bb = j
            lstt[bb][aa] = k[-1]
    return(lstt)
    


        



