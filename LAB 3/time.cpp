#include<iostream>
using namespace std;
class time
{
public:
	int hours,minutes,seconds;
	time()
	{
		hours=0;
		minutes=0;
		seconds=0;
	}
	time(int x, int y, int z)
	{
		hours=x;
		minutes=y;
		seconds=z;
	}
	void display()
	{
		cout<<"Time in hh:mm:ss is "<<hours<<":"<<minutes<<":"<<seconds<<endl;
	}
};
int main()
{
	time s;
	int x,y,z;
	cout<<"Enter time of your clock in hh:mm:ss ";
	cin>>x>>y>>z;
	time m(x,y,z);
	display();
}