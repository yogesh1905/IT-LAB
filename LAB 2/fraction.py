class fraction:
	def __init__(self,a,b):
		self.a=a;
		self.b=b;
	def __str__(self):
		return str(self.a)+"/"+str(self.b)
	def inverse(self):
		return str(self.b)+"/"+str(self.a)
	def __add__(self,other):
		nu=self.a*other.b+self.b*other.a
		de=self.b*other.b
		for i in range(2,min(nu,de)+1):
			if(nu%i==0 and de%i==0):
				newnu=nu//i
				newde=de//i
		return fraction(newnu,newde)
	def __mul__(self,other):
		nu=self.a*other.a
		de=self.b*other.b
		for i in range(2,min(nu,de)+1):
			if(nu%i==0 and de%i==0):
				newnu=nu//i
				newde=de//i
		return fraction(newnu,newde)
	def __eq__(self,other):
		if(self.a/self.b==other.a/other.b):
			return True
		else:
			return False


def main():
	a,b=input("Enter numerator and denominator: ").split()
	a=int(a)
	b=int(b)
	fr1=fraction(a,b)
	a,b=input("Enter numerator and denominator: ").split()
	a=int(a)
	b=int(b)
	fr2=fraction(a,b)
	while(True):
		print("What do you want to do?\n a)add \n b)inverse \n c)multiply \n d)check for equality\n e)exit")
		temp=input()
		if(temp=='a'):
			print(fr1+fr2)
		elif(temp=='b'):
			print(fr1.inverse())
		elif(temp=='c'):
			print(fr1*fr2)
		elif(temp=='d'):
			print(fr1==fr2)
		elif(temp=='e'):
			return
		else:
			print("Invalid input.")

main()