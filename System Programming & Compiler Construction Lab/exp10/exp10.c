#include<stdio.h>
#include<conio.h>
char a[100][100];
int c[10];
int count=0;
int main(){
    int n,i,j;
    printf("Enter the number of productions>>>");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("Enter production Number %d>>> ",i+1);
        scanf(" %s",a[i]);
    }
    for(i=0;i<n;i++){
        for(j=1;a[i][j]!='\0';j++){
            if(a[i][j]=='=' || a[i][j]=='+' || a[i][j]=='*' || a[i][j]=='-' || a[i][j]=='/'){
                count++;
            }
        }
        c[i]=count;
        count=0;
    }
    printf("The count of operators in each of the profductions is>>\n");
    for(i=0;i<n;i++){
        printf("For production:%d -> %d\n",i,c[i]);
    }
    printf("<<<<STARTING CODE GENERATION>>>>");
    for(i=0;i<n;i++){
        if(c[i]==1){
            j=2;
            printf("\nMOV R%d,%c",i,a[i][j]);
            j=0;
            printf("\nMOV %c,R%d",a[i][j],i);
        }
        else{
            
            switch(a[i][3]){
                case '+':
                printf("\nMOV R%d,%c",i,a[i][2]);
                printf("\nADD R%d,%c",i,a[i][4]);
                printf("\nMOV %c,R%d",a[i][0],i);
                break;
                case '-':
                printf("\nMOV R%d,%c",i,a[i][2]);
                printf("\nSUB R%d,%c",i,a[i][4]);
                printf("\nMOV %c,R%d",a[i][0],i);
                break;
                case '*':
                printf("\nMOV R%d,%c",i,a[i][2]);
                printf("\nMUL R%d,%c",i,a[i][4]);
                printf("\nMOV %c,R%d",a[i][0],i);
                break;
                case '/':
                printf("\nMOV R%d,%c",i,a[i][2]);
                printf("\nDIV R%d,%c",i,a[i][4]);
                printf("\nMOV %c,R%d",a[i][0],i);
                break;
                default:
                printf("\nEXIT");
                break;
            }
        }
    }
    printf("\n<<<<CODE GENERATED>>>>");
}

