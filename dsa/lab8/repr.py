#print adj matrix and list

class Graph:
    def __init__(self, V = 0, E = 0):
        self.V = V
        self.E = E
        self.matrix = [[0] * V for i in range(0,V)]
        self.adjList = [[] for i in range(0,V)]
        self.visited = [0 for i in range(self.V)]
        self.dist = [-1 for i in range(self.V)]
    
    def insert(self, x, y, undirected = 0):
        self.adjList[x].append(y)
        if undirected == 0:
            self.adjList[y].append(x)

        self.matrix[x][y] = 1
        if undirected == 0:
            self.matrix[y][x] = 1
    
    def printMatrix(self):
        for i in range (0, self.V):
            for j in range(0, self.V):
                print(self.matrix[i][j], end = " ")
            print()
    def printList(self):
        for i in range(0, self.V):
            print(i, end = ": ")
            for j in range(0, len(self.adjList[i])):
                print(self.adjList[i][j], end = " ")
            print()
    def input(self):
        for i in range(0, self.E):
            x, y = [int(j) for j in input().split()]
            self.insert(x, y)
def main():
    print("num vertices: ", end="")
    v = int(input())
    print("num edges: ", end="")
    e = int(input())

    G = Graph(v, e) 
    for i in range(0, e):
        x, y = [int(j) for j in input().split()]
        G.insert(x, y)
    
    G.printList()
    print()
    G.printMatrix()
if __name__ == '__main__':
    main()