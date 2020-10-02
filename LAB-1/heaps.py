class heap:
	def __init__(self):
		self.ar=[]
		self.k=-1
	def insert(self,x):
		self.ar.insert(self.k,x)
		self.heapifyup(self.k)
		self.k=self.k+1
		print("here",self.k)
	def heapifyup(self,x):
		x=x+1
		par=x//2
		if(x>1):
			while((par>=1) and (self.ar[par-1]<self.ar[x-1])):
				self.ar[par-1],self.ar[x-1]=self.ar[x-1],self.ar[par-1]
				x=x//2
				par=x//2
	def heapifydown(self,x):
		par=x+1
		c1=2*par
		c2=c1+1
		if(((self.k+1)%2)==1):
			while((c2<=self.k+1) and (self.ar[par-1]<self.ar[c1-1] or self.ar[par-1]<self.ar[c2-1])):
				if(self.ar[c1-1]>self.ar[c2-1]):
					self.ar[par-1],self.ar[c1-1]=self.ar[c1-1],self.ar[par-1]
					par=c1
					c1=2*par
					c2=2*par+1
				else:
					self.ar[par-1],self.ar[c2-1]=self.ar[c2-1],self.ar[par-1]
					par=c2
					c1=2*par
					c2=2*par+1
		else:
			while((c1<self.k+1) and (self.ar[par-1]<self.ar[c1-1] or self.ar[par-1]<self.ar[c2-1])):
				if(self.ar[c1-1]>self.ar[c2-1]):
					self.ar[par-1],self.ar[c1-1]=self.ar[c1-1],self.ar[par-1]
					par=c1
					c1=2*par
					c2=2*par+1
				else:
					self.ar[par-1],self.ar[c2-1]=self.ar[c2-1],self.ar[par-1]
					par=c2
					c1=2*par
					c2=2*par+1
			if((c1==self.k+1) and (self.ar[par-1]<self.ar[c1-1])):
				self.ar[par-1],self.ar[c1-1]=self.ar[c1-1],self.ar[par-1]
	def extractmax(self):
		print(self.ar[0])
		self.ar[0]=self.ar[self.k]
		self.k=self.k-1
		self.heapifydown(0)
	def display(self):
		for i in range(0,self.k+1):
			print(self.ar[i])
def main():
	h=heap()
	h.insert(10)
	h.insert(11)
	h.insert(2)
	h.insert(30)
	h.insert(19)
	h.display()
	print("Extracting max")
	h.extractmax()
	h.extractmax()
	h.extractmax()
	h.insert(99)
	h.insert(100)
	h.extractmax()
	h.display()
if __name__=='__main__':
        main()
