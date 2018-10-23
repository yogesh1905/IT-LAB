from repr import Graph
import bfs

def explore(G):
    visited = [0 for i in range(G.V)]
    dist = [0 for i in range(G.V)]

    print("components")
    for i in range(G.V):
        if G.visited[i] == 0:
            bfs.BFS(G, i)
        
def main():
    print("num vertices: ", end="")
    v = int(input())
    print("num edges: ", end="")
    e = int(input())
    G = Graph(v,e)
    print("input: ")
    G.input()
    #print()
    #G.printList()
    print()
    explore(G)

if __name__ == '__main__':
    main()