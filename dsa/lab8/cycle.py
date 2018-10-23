from repr import Graph

def DFS(G, source, current):
    G.visited[source] = 1
    current[source] = 1
    
def detectCycle(G):
    current = [None for i in range(G.V)]
    for i in range(G.V):
        if G.visited == 0:
            c = DFS(G, i, current)
            if c == True:
                print("Cycle exists")
            else:
                print("No Cyle")
def main():
    print("num vertices: ", end="")
    v = int(input())
    print("num edges: ", end="")
    e = int(input())

    G = Graph(v, e)
    G.input()

    detectCycle(G)