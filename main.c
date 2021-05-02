#include <stdio.h>
#include <stdlib.h>

struct node {
   int dados;
   struct node *proximo_num;
};

struct node *cabeca = NULL;
struct node *atual_num = NULL;

//display the list
void printList() {

   struct node *ptr = cabeca;

   printf("\n[head] =>");
   //start from the beginning
   while(ptr != NULL) {        
      printf(" %d =>",ptr->dados);
      ptr = ptr->proximo_num;
   }

   printf(" [null]\n");
}

//insert link at the first location
void insert(int dados) {
   //create a link
   struct node *link = (struct node*) malloc(sizeof(struct node));

   //link->key = key;
   link->dados = dados;

   //point it to old first node
   link->proximo_num = cabeca;

   //point first to new first node
   cabeca = link;
}

int main() {
   insert(10);
   insert(20);
   insert(30);
   insert(1);
   insert(40);
   insert(56); 

   printList();
   return 0;
}