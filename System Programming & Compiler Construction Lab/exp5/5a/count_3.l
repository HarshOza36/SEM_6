%option noyywrap
%{
	#include<stdio.h>
	int lines=0;
	int words=0;
	int spaces=0;
	int chars=0;
%}

%%
[A-Za-z]   {chars++;}
\n          {lines++;words++;}
" "|"	"   {spaces++;words++;}
"$"         {printf("\ntotal lines: %d\n total words: %d\n total spaces: %d\n total characters: %d\n",lines,words,spaces,chars);}

%%
int main()
{

	printf("enter the string; \n");
	yylex();
	return 0;
}