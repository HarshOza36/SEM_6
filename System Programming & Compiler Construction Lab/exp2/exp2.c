#include<stdio.h>
#include<conio.h>
#include<string.h>

int main(){
	int a,b,i,len,ctr=0,ctr1=0;
	char s[100],*word[5]={"if","If","then","Then"},res,res2,res3,res4;
	char *action[6]={"this","that","there","it","they"};
	char *s1[100];
	printf("Enter the state for lexical analyzing!>>>>");
	gets(s);
/*	  printf("%s",s);
	printf("\n");*/
	i=0;
	s1[i]=strtok(s," ");
	while(s1[i]!=NULL){
		
		s1[++i]=strtok(NULL," ");
	}
	len=i;
	for(i=0;i<len;i++){
		/*printf("%s\n",s1[i]);*/
		res = strcmp(s1[i],word[0]);
		res2=strcmp(s1[i],word[1]);
		res3=strcmp(s1[i],word[2]);
		res4=strcmp(s1[i],word[3]);
		if(res2==0 || res==0 || res3==0 || res4==0){
			printf("KEYWORD:%s\n",s1[i]);
		}
		else if(strcmp(s1[i],action[0])==0||strcmp(s1[i],action[1])==0||strcmp(s1[i],action[2])==0||strcmp(s1[i],action[3])==0||strcmp(s1[i],action[4])==0)
    	{	++ctr1;
     		printf("ACTION(%d):%s\n",ctr1,s1[i]);	 
		}
		else{
			++ctr;
			printf("NOUN(%d):%s\n",ctr,s1[i]);
		}
		
	}
}


