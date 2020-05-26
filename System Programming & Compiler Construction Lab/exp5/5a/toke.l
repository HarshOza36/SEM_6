%option noyywrap
%{
	#include<stdio.h>
	int keyword=0;
	int datatype=0;
	int symbol=0;
	int identifier=0;
	int number=0;
	int t=0;
%}

%%
"if"|"else"|"while"|"dowhile"|"for"|"int"|"float"|"long"|"char"|"double"|"printf"|"break"  {printf("keyword\n");keyword++,t++;}
"("|")"|";"|","|"{"|"}"|"%"|"<"|">"|"!"|"&"|":"|"+"|"-"|"\""|"="|"$"|"@"	   {printf("symbols \n");symbol++;t++;}
[A-Za-z]+          {printf("Identifier\n");identifier++;t++;}
[0-9]+	           {printf("number\n");number++,t++;}
\n                 {printf("\nKeywords=%d\n Symbols=%d\n Identifiers=%d\n Numbers=%d\n Tokens=%d\n",keyword,symbol,identifier,number,t);}
%%
int main()
{
	printf("enter the string");
	yylex();
	return 0;
 }