from collections import deque
def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 

    file=open('input.txt','r')
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
    stack=[]
    time=0
    u=0
    while(len(stack)>0):
        stack.append(u)
        visited[u]=1
        start[u]=time
        time+=1
        for v in G[u]:
            if(visited[v]==0):
                pred[v]=u
                u=v
                stack.append(v)
                visited[v]=1
        if(visited[G[u][i]]==0 for i in range(len(G))):
            continue
        else:
            finish[u]=time
            time+=1
    for i in range(len(G)):
        print("vertex:",i,"start:",start[i],"finish:",finish[i])
        for j in range(len(G[i])):
            if(pred[i]==G[i][j] or pred[G[i][j]]==i):
                print("Tree edge:",i,G[i][j])
            else:
                print("Back edge:",i,G[i][j])


if __name__ == '__main__':
    main()