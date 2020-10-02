time=0

def twoEC(G,u,visited,start,finish,pred):
    global time
    visited[u]=1
    start[u]=time
    time+=1
    sst=start[u]
    if(u==0):
        sst=99999
    for v in G[u]:
        if(visited[v]==0):
            pred[v]=u
            sst=min(twoEC(G,v,visited,start,finish,pred),sst)
        elif(pred[u]!=v):
            sst=min(start[v],sst)
        #print(u,sst)
    if(sst==start[u] and u!=0):
        return -1
    finish[u]=time
    time+=1
    
    return sst;

def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 

    file=open('input2.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for node in line.split(' '):
            if first:
                first=False
                continue
            adjacentVertices.append(int(node))
        G.append(adjacentVertices)

    file.close()
    start=[0 for i in range(len(G))]
    finish=[0 for i in range(len(G))]
    visited=[0 for i in range(len(G))]
    pred=[0 for i in range(len(G))]
    #print(G)
    print(twoEC(G,0,visited,start,finish,pred)>=0)


if __name__ == '__main__':
    main()