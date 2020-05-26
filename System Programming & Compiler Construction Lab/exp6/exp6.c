#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>

int m=0,n,p,ct;
char a[15][15], t[15], op[15][15],ch;
int oppr(char x1, char y);
int oper(char x);

int main(){
int i,j,k,flag,z;

printf("Enter The No. of Productions:>>>>");
scanf("%d",&n);
z=0;
printf("Enter The Productions:>>>>\n");
for(i=0;i<n;i++){
	scanf("%s%c",&a[i],&ch);
}
flag=0;
for(i=0;i<n;i++){
	for(j=3;a[i][j]!='\0';j++){
		if(a[i][j]!=' ' && (a[i][j]<65 || a[i][j]>90))
		{
			flag=0;
			for(k=0;k<z;k++)
			{
				if(a[i][j]==t[k])
				{
					flag=1;
					break;
				}
			}
			if(flag==0){
				t[z++]=a[i][j];
			}

		}
	
	}
}
t[z++]='$';
ct=z;

for(i=0;i<z;i++)
{
	for(j=0;j<z;j++)
	{
		op[i][j]=oppr(t[i],t[j]);
	}
}

j=z-1;
op[j][j]=6;
printf(" \n ");
for(i=0;i<z;i++)
{
	printf("   %c",t[i]);
}
for(i=0;i<z;i++)
{	
	printf("\n %c ",t[i]);
	for(j=0;j<z;j++)
	{
		if(op[i][j]==1)
		printf("  .>");
		else if(op[i][j]==2)
		printf("  .=");
		else if(op[i][j]==3)
		printf("  <.");
		else if(op[i][j]==4)
		printf("   -");
		else printf("   accept");
	}	 
		
}
return 0;

}

int oppr(char x1, char y)
{
	int m,n;
	m=oper(x1);
	n=oper(y);
	if(m==4 && n==4)
	return 4;
	if(m>=n)
	return 1;
	else
	return 3;
}

int oper(char x)
{
	if(x=='+' || x=='-')
	 return 1;
	else if(x=='*' || x=='/')
	 return 2;
	else if(x=='^')
	 return 3;
	else if(x=='$')
	 return 0;
	else
	 return 4;
}

