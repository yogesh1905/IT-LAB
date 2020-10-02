class stack:
	def __init__(self):
		self.top=-1
		self.list=[]
	def push(self,a):
		self.list.append(a)
		self.top=self.top+1
	def pop(self):
		if(self.top!=-1):
			del self.list[self.top]
			self.top=self.top-1
		else:
			print("Stack empty.")
	def __str__(self):
		return str(self.list)
def main():
	st=stack()
	while(True):
		print("What do you want to do?\n a)push \n b)pop \n c)display \n d)exit")
		temp=input()
		if(temp=='a'):
			a=int(input("Enter element: "))
			st.push(a)
		elif(temp=='b'):
			st.pop()
		elif(temp=='c'):
			print(st)
		elif(temp=='d'):
			return
		else:
			print("Invalid input.")

main()