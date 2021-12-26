#include<iostream>
#include<string>
#include<vector>
using namespace std;
int op(int i, int j=1){
	return i*j;
}
int op(char a, char b){
	return b-a;
}

int op(float x, float y){
	return x/y;
}
int main(){
	int i,k=1;
	for(i=0;i<3;i+=2)
	k++;
	cout<<k;
}