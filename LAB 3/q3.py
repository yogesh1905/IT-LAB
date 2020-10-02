from collections import deque

def bipartite(G,s):
    visited=[]
    queue=deque([])
    color={}
    visited.append(s)
    color[s]=0
    queue.append(s)
    #print("vertex :",s,"color :",color[0])
    while(len(queue)!=0):
        temp=queue.popleft();
        for u in G[temp]:
            if(u not in visited):
                visited.append(u)
                color[u]=1-color[temp]
                queue.append(u)
            if(color[u]==color[temp]):
                return False
    return True



def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 

    file=open('input3.txt','r')
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
    if(bipartite(G,0)):
        print("It is bipartite.")
    else:
        print("It is not bipartite.")

if __name__ == '__main__':
    main()