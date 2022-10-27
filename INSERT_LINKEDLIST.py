class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked:
    def __init__(self):
        self.head=None
        self.lastnode=None
    def append(self,data):
        if self.lastnode==None:
            self.head=node(data)
            self.lastnode=self.head
        else:
            self.lastnode.next=node(data)
            self.lastnode=self.lastnode.next
    def insert(self,data):
        new=node(data)
        new.next=self.head
        self.head=new
    def insertend(self,data):
        new=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
    def insertpos(self,pos,data):
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new=node(data)
        new.next=temp.next
        temp.next=new
    def println(self):
        if self.head==None:
            print('empty')
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end=' ')
                temp=temp.next
l=linked()
a=int(input())
for i in range(a):
    data=int(input('enter:'))
    l.append(data)
a=int(input('insert:'))
l.insert(a)
b=int(input('last:'))
l.insertend(b)
c=int(input('pos:'))
d=int(input('data:'))
l.insertpos(c,d)
l.println()                