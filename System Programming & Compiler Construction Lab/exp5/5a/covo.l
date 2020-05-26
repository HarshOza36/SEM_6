%option noyywrap
%{
	#include<stdio.h>
	int v=0;
	int c=0;
%}

%%
[aeiouAEIOU]	{printf("Vowel\n");v++;}
[A-Za-z]	{printf("Consonants\n");c++;}
\n	{printf("\nVowels=%d\nConsants=%d\n",v,c);}
%%
int main()
{
	printf("enter the string");
	yylex();
	return 0;
}