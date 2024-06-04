class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class LinlList:
    def __init__(self):
        self.head=None
    def pp(self):
        temp=self.head
        while(temp):
            print(temp.data , end="")
            if(temp.next!=None):
                print("->",end="")
            temp=temp.next
    def inserthead(self,data):
        newnode=Node(data)
        if(self.head==None):
            self.head=newnode
            return


        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
    def insertend(self,data):
        newnode=Node(data)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
    def insertAtposition(self,i,data):
        if(i==0):
            self.inserthead(data)
            return
        temp=self.head
        c=0
        newnode=Node(data)
        while(c<i-1 and temp):
            c+=1
            temp=temp.next

        if(temp==None):
            return
        if(temp.next==None):
            self.insertend(data)
        t2=temp.next
        newnode.next=t2
        newnode.prev=temp
        temp.next=newnode
        t2.prev=newnode
      

if __name__ == '__main__':
    ll=LinlList()
    
    ll.inserthead(40)
    ll.insertend(40)
    ll.insertAtposition(2,300)
    ll.insertAtposition(7,11111)
    ll.pp()






class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist:
    def __init__(self):
        self.head=None
    def addhead(self,data):
        n=node(data)
        n.next=self.head
        self.head=n
    def addend(self,data):
        n=node(data)
        if(self.head==None):
            self.head=n
            return
        t=self.head
        while(t.next):
            t=t.next
        t.next=n
    def pp(self):
        t=self.head
        while t:
            print(t.data,end="")
            if(t.next!=None):
                print(" --> ",end="")
            t=t.next
    def addpos(self,i,data):
        n=node(data)
        if(i==0):
            self.addhead(data)
            return
        c=0
        t=self.head
        while(c<i-1 and t):
            c=c+1
            t=t.next
        if t==None:
            print("invalid")
            return
 
        n.next=t.next
        t.next=n

    def inserdatas(self,data):
        for i in data:
            self.addend(i)



ll=Linklist()
ll.inserdatas(["python","data structures","algorithms","complexity"])
ll.addhead(1)
ll.addend(3)
ll.addend(2)
ll.addend(1)
ll.addpos(0,100)
ll.pp()
