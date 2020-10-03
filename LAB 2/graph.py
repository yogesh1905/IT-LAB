class graph:
	def __init__(self,n):
		self.n=n
		self.adlist=[[] for i in range(n)]
		self.admat=[[0 for i in range(n)] for j in range(n)]
	def insert(self,a,b):
		self.adlist[a].append(b)
		self.adlist[b].append(a)
		self.admat[a][b]=1
		self.admat[b][a]=1
	def adList(self):
		print("The adjacency list is: ")
		for i in range(len(self.adlist)):
			print("Vertex ",i,":",sep="",end="")
			for j in range(len(self.adlist[i])):
				print(self.adlist[i][j],"",sep=",",end="")
			print("")
	def adMat(self):
		print("The adjacency matrix is: ")
		for i in range(self.n):
			for j in range(self.n):
				print(self.admat[i][j],"",end="")
			print("")

def main():
	n=int(input("Enter number of vertices: "))
	edges=int(input("Enter number of edges: "))
	gr=graph(n)
	for i in range(edges):
		a,b=list(map(int,input().split()))
		gr.insert(a,b)
	gr.adMat()
	gr.adList()

main()

