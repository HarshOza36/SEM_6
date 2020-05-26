#include<stdio.h>
#include<conio.h>
#include<string.h>
void main()
{	int i=0,n,j=3;
	char a,b,s[10][10],nt,a1;
	clrscr();
	printf("Enter the number of productions>>");
	scanf("%d",&n);
	printf("Enter the Productions in form A->Aa|b >>>>");
	for(i=0;i<n;i++){
		scanf("%s",s[i]);
	}
	printf("\n");
	for(i=0;i<n;i++)
	{	printf("%s",s[i]);
		nt=s[i][0];
		if(nt==s[i][j])
		{
			a=s[i][j+1];
			a1=s[i][j+2];
			printf("         <<<Left Recursion Found>>>\n");
			while(s[i][j]!=0 && s[i][j]!='|')
			{j++;}
			if(s[i][j]!=0)
			{	b=s[i][j+1];
				printf("\nGrammar After Eliminating Left Recursion>>>\n");
				printf("%c -> %c%c\'",nt,b,nt);
				printf("\n%c\' -> %c%c%c\'|EP\n",nt,a,a1,nt);
			}
			else{
			    printf("\nNO further Reductions possible\n");
			}
		}
		else{
			printf("         <<<IS NOT LEFT RECURSION>>>\n");
		}
		j=3;
	}
	getch();
}

