%option noyywrap
%{
	#include<stdio.h>
%}
%%
"hello world" printf("Hi everyone out there!!!!!");
.;
%%
int main()
{
        yylex();
	return 0;
}