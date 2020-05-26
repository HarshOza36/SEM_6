%option noyywrap
%{
	#include<stdio.h>
	int a=0;
	int b=0,op=0;
	float c=0;
%}

%%
[0-9]+ {
if(op==0)
a=atof(yytext);
else
{
b=atof(yytext);
switch(op)
{
case 1: c=a+b;
break;
case 2: c=a-b;
break;
case 3: c=a*b;
break;
case 4: c=a/b;
break;
}
}
}
"+" {op=1;}
"-" {op=2;}
"*" {op=3;}
"/" {op=4;}
\n {printf("answer =%f\na=%d\nb=%d\n",c,a,b);}

%%
int main()
{
	yylex();
	return 0;
}