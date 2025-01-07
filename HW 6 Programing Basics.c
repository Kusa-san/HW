#include<stdio.h>

char name[20];

void printName(char name[]){
    printf("My name is %s\n", name);
}

int main(){

    printName("bisha");

    return 0;
}