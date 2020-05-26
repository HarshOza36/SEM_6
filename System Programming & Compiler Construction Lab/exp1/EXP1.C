#include<stdio.h>
#include<stdio.h>
#include "hmath.h"
void main(){
	int a,b,ch,res;
	clrscr();
	printf("Enter a and b>>");
	scanf("%d %d",&a,&b);
	printf("\n_______________________MENU________________\n");
	printf("1.ADDITION 2.SUBTRACTION 3.DIVISION 4.MULTIPLICATION\n");
	printf("5.MODULO 6.FACT of A 7.SQUARE OF A 8.GREATER NUMBER\n");
	printf("To exit enter 0\n");
	while(ch!=0){
		printf("\nENTER YOUR CHOICE>>");
		scanf("%d",&ch);
		switch(ch){
			case 1:
			res=add(a,b);
			printf("Addition is %d",res);
			break;
			case 2:
			printf("Subtraction is %d",sub(a,b));
			break;
			case 3:
			printf("Division is %d",div(a,b));
			break;
			case 4:
			printf("Multiplication is %d",mul(a,b));
			break;
			case 5:
			printf("Modulo is %d",mod(a,b));
			break;
			case 6:
			printf("Factorial of A is %d",fact(a));
			break;
			case 7:
			printf("Square of a is %d",square(a));
			break;
			case 8:
			checkGreater(a,b);
			break;
			default:
			printf("EXIT!!!");
			break;
		}
	}
	getch();
}