#singly linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
a=node(1)
b=node(2)
c=node(3)

a.next = b
b.next = c


#doubley linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
a=node(1)
b=node(2)
c=node(3)

a.next = b
b.prev = a
b.next = c
c.prev = b
head=a
print(head.next.data)
print(head.next.prev.data)


#circular linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next = None
a=node(1)
b=node(5)
c=node(9)

a.next=b
b.next=c
c.next=a #circular

head = a
curr=head
while True:
    print(curr.data,end=" ")
    curr=curr.next
    if curr==head :
        break

