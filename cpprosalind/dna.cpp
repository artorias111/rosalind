// /usr/bin/g++ - you don't need a shebang line for cpp
#include <iostream>
#include <fstream> //file i/o
using namespace std;

int main(){
	cout<<"hello world";
	fstream x;
	x.open("data/rosalind_dna.txt",ios::in);
	return 0;
}
