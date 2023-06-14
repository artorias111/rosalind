#include <iostream>
using namespace std;

int fib(int x){
	if(x==1)
		return 1;
	if(x==0)
		return 0;
	return fib(x-1)+fib(x-2);
} 

int main(){
	cout<<"Enter your number\n";
	int n;
	cin>>n;
	int a;
	a=fib(n);
	cout<<a<<"\n";
}
