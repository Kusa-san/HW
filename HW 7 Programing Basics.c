#include<stdio.h>

char name[20];
char op[20];
int num1,num2;
int i=0;
int main() {

    // printf("Enter your name: ");
    // fgets(name,20,stdin);

    // printf("Greetings %s\nenter the first number: ",name);
    // scanf("%d",&num1);

    // printf("\nEnter the second number: ");
    // scanf("%d",&num2);

    // printf("Enter the operation: ");
    // scanf(" %c",&op);

    // switch(op){
    //     case '+':
    //         printf("The sum of %d and %d is %d\n",num1,num2,num1+num2);
    //         break;
    //     case '-':
    //         {if(num1>num2)
    //             printf("The difference of %d and %d is %d\n",num1,num2,num1-num2);
    //             else
    //             printf("The difference of %d and %d is %d\n",num2,num1,num2-num1);
    //         }
    //         break;
    //     case '*':
    //         printf("The product of %d and %d is %d\n",num1,num2,num1*num2);
    //         break;
    //     case '/':
    //         printf("The division of %d and %d is %d\n",num1,num2,num1/num2);
    //         break;
    //     default:
    //         printf("Invalid operation\n");
    // }

    printf("Enter your name: ");
    fgets(name,20,stdin);

    printf("Greetings %s",name);

    printf("Enter the operations with single digit numbers and no spaces:\n");
    fgets(op,sizeof(op),stdin);

    while (op[i]!='\0')
    {
        if(op[i]=='+')
            printf("the sum of %d and %d is %d",(op[i-1]-48),(op[i+1]-48),(op[i-1]-48)+(op[i+1]-48));
        
        else if(op[i]=='-')
            printf("the difference of %d and %d is %d",(op[i-1]-48),(op[i+1]-48),(op[i-1]-48)-(op[i+1]-48));
        
        else if(op[i]=='*')
            printf("the product of %d and %d is %d",(op[i-1]-48),(op[i+1]-48),(op[i-1]-48)*(op[i+1]-48));
        
        else if(op[i]=='/')
                printf("the division of %d and %d is %d",(op[i-1]-48),(op[i+1]-48),(op[i-1]-48)/(op[i+1]-48));

            else
            printf("Invalid operation\n");
        
        i++;
    }
    
    return 0;
}