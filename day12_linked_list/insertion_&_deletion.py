#linked list 
#syntax
class node:
    def __init__(self,num):
        self.num = num
        self.next=None

a=node(1)
b=node(2)
c=node(3)
d=node(4)

a.next=b
b.next=c
c.next=d

head = a

print(head.num)
print(head.next.next.num)

#traverse in linked list
def printlinkedlist(head):
    while head!=None :
        print(head.num,end=" ")
        head=head.next
    print()
printlinkedlist(head)


# inserting new element at the begining
newnode=node(0)
newnode.next=head
head=newnode
printlinkedlist(head)

#insertion at last
newnode=node(9)
curr=head
while curr.next!=None :
    curr=curr.next
curr.next=newnode
printlinkedlist(head)

#insertion at kth index
k=3
newnode=node(7)
curr=head
for i in range(k-1):
    curr=curr.next
newnode.next=curr.next
curr.next=newnode
printlinkedlist(head)

#delete first of linked list
head=head.next
printlinkedlist(head)

#delete last element of linked list
curr=head
while curr.next.next!=None :
    curr=curr.next
curr.next=None
printlinkedlist(head)

#delete kth element of linked list
k=4
curr=head
for i in range(k-1):
    curr=curr.next
curr.next = curr.next.next
printlinkedlist(head)