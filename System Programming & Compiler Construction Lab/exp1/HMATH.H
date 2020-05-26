#include<stdio.h>
#include<conio.h>
int add(int a,int b){
	int c;
	c=a+b;
	return c;
}
int sub(int a,int b){
	int c;
	c=a-b;
	return c;
}
int mul(int a,int b){
	int c;
	c=a*b;
	return c;
}
int div(int a,int b){
	int c;
	c=a/b;
	return c;
}
int mod(int a,int b){
	int c;
	c=a%b;
	return c;
}
int square(int a){
	int c;
	c=a*a;
	return c;
}
int fact(int a){
	if(a==1){
		return 1;
	}
	else if(a>1){
		return ((a)*fact(a-1));
	}
	else{
		return 0;
	}
}
void checkGreater(int a , int b){
	if(a>b){
		printf("%d is greater than %d\n",a,b);
	}
	else{
		printf("%d is greater than %d\n",b,a);
	}
}