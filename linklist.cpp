#include<bits/stdtr1c++.h>
using namespace std;

class node{
    public:
    int data;
    node* next;
    node(int val){
        data=val;
        next=NULL;
    }
};
void addfirst(node* &head,int val){
    node* n=new node(val);
    n->next=head;
    head=n;
}
void addlast(node* &head,int val){
    node* n=new node(val);
    if(head==NULL){
        head=n;
        return;
    }
    node* t=head;
    while(t->next!=NULL){
        t=t->next;
    }
    t->next=n;
}
void display(node* &head){
    node* t=head;
    while(t!=NULL){
        cout<<t->data;
        if(t->next!=NULL){
            cout<<"-->";
        }
        t=t->next;
    }
}


int main(){
    node* head=NULL;
    addfirst(head,12);
    addfirst(head,13);
    addlast(head,13);
    addlast(head,14);
    display(head);
    return 0;
}
