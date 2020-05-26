%{
	#include <stdio.h>
	#include <math.h>
	#include <stdlib.h>
%}
%token NUM
%left '+' '-'
%%

stmt : exp   {printf("\n Answer: %d \n", $1);}
	;

exp :	exp '+' exp {$$=$1+$3;}
	| exp '-' exp {$$=$1-$3;}

	| NUM	{$$=$1;}
	;

%%

int main()
{
	printf("Enter the regular expression \n");
	yyparse();
	printf("Valid expression! ");
	return 0;

}
yyerror()
{
 printf("Invalid expression!");
 exit(0);
}

int yywrap()
{
 return 1;
}
