#include<stdio.h>

char name[20];
int num1,num2;
char op;

int main(){

    printf("Enter your name: ");
    fgets(name,20,stdin);

    printf("Greetings %s\nenter the first number: ",name);
    scanf("%d",&num1);

    printf("\nEnter the second number: ");
    scanf("%d",&num2);

    printf("Enter the operation: ");
    scanf(" %c",&op);

    switch(op){
        case '+':
            printf("The sum of %d and %d is %d\n",num1,num2,num1+num2);
            break;
        case '-':
            {if(num1>num2)
                printf("The difference of %d and %d is %d\n",num1,num2,num1-num2);
                else
                printf("The difference of %d and %d is %d\n",num2,num1,num2-num1);
            }
            break;
        case '*':
            printf("The product of %d and %d is %d\n",num1,num2,num1*num2);
            break;
        case '/':
            printf("The division of %d and %d is %d\n",num1,num2,num1/num2);
            break;
        default:
            printf("Invalid operation\n");
    }

    return 0;
}