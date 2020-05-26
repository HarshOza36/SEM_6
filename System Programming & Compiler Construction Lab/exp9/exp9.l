
%{
	#include"y.tab.h"
%}
%%
[a-zA-Z]+ 	{strcpy(yylval.str,yytext);   return Var;}
[0-9]+		{strcpy(yylval.str,yytext);   return Num;}	
\n		{return 0;}
.		{return yytext[0];}
%%
int yywrap()
{
	return 1;
}





