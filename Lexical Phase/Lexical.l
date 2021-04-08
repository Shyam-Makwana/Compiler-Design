%{
#include <stdio.h>
%}

Digit [0-9]
ID [a-zA-Z][a-zA-Z0-9]*

%%

"/*"({ID}[ \n\t]*{ID}[ \n\t]*)*"*/"	{printf("< Multiline Comment , %s >\n",yytext);}

{Digit}+	{printf("< Integer , %s >\n",yytext);}

{Digit}*"."{Digit}+	{printf("< Float , %s >\n",yytext);}

"if"|"for"|"while"|"do"|"exit"|"else"|"case"|"switch"|"until"	{printf("< Keyword , %s >\n",yytext);}

{ID}	{printf("< ID , %s >\n",yytext);}

"***"[a-zA-Z0-9_., "]*	{printf("< Single line comment , %s >\n",yytext);}

"'"[a-zA-Z0-9]*"'"	{printf("< String constant , %s >\n");}

"("|")"|"{"|"}"|";"|","|"["|"]"	{printf("< Punctuation , %s >\n",yytext);}

":="|"<>"|"=="|"!="|"<="|">="|"+"|"-"|"*"|"%"|"\""	{printf("< Operator , %s >\n",yytext);}

[ \t]	{}

. {printf("<Invalid Token : %s >\n",yytext);}
%%

int yywrap(){}
int main()
{
	yylex();
	return 0;
}