 /* @author: ANISHK YADAV */

%{
#include<stdio.h>
#include<string.h>
int count=0;
%}
%%
[A-Z] {printf("%s CAPITAL LETTER\n", yytext); count++;}
. {printf("%s NOT A CAPITAL LETTER\n", yytext);}
\n {return 0;}
%%

int yywrap()
{
return 1;
}

int main()
{
yylex();
printf("\n No Of captials:%d", count);
return 0;
}