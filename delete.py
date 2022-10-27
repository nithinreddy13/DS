class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
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
    def dele(self):
        temp=self.head
        self.head=None
        self.head=temp.next
    def delend(self):
        temp=self.head.next
        priv=self.head
        while temp.next is not None:
            temp=temp.next
            priv=priv.next
        priv.next=None
    def delpos(self,pos):
        temp=self.head.next
        priv=self.head
        for i in range(pos-1):
            temp=temp.next
            priv=priv.next
        priv.next=temp.next

    def println(self):
        if self.head==None:
            print('empty')
        else:
            temp=self.head
            while temp is not None:
                print(temp.data)
                temp=temp.next
list=sll()
a=int(input('no of elements:'))
for i in range(a):
    data=int(input('enter:'))
    list.append(data)
list.dele()
list.delend()
list.delpos(2)
list.println()