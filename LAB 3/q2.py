from collections import deque

def bfs(G,s):
    visited=[]
    queue=deque([])
    dist={}
    visited.append(s)
    dist[s]=0
    queue.append(s)
    #print("vertex :",s,"Distance :",dist[0])
    while(len(queue)!=0):
        temp=queue.popleft();
        for u in G[temp]:
            if(u not in visited):
                visited.append(u)
                dist[u]=dist[temp]+1
                queue.append(u)
                #print("vertex :",u,"Distance :",dist[u])
    return visited

def connected(G):
    visited=[]
    for v in range(len(G)):
        if(v not in visited):
            newv=bfs(G,v)
            print(newv)
            visited.extend(newv)


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
    connected(G)
    #print(G)

if __name__ == '__main__':
    main()