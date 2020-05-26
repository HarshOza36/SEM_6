%option noyywrap
%{
	#include<stdio.h>
	int count1=0;
	int count2=0;
%}

%%
[a-z] { printf("lower case\n");count1++; }
[A-Z] { printf("upper case\n");count2++; }
\n    { printf("\nupper case= %d\nlower case= %d\n",count2,count1);}
.	;
%%
int main()
{
	printf("  enter the string    ");
	yylex();
	return 0;
}