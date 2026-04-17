class node:
    def __init__(self,num):
        self.num = num
        self.next=None

a=node(1)
f=node(1)
b=node(2)
c=node(3)
g=node(3)
d=node(4)
e=node(5)
h=node(5)
i=node(5)
j=node(5)
k=node(5)

a.next=f
f.next=b
b.next=c
c.next=g
g.next=d
d.next=e
e.next=h
h.next=i
i.next=j
j.next=k

head = a
def printlinkedlist(head):
    curr=head
    while curr!=None :
        print(curr.num,end=" ")
        curr=curr.next
    print()
printlinkedlist(head)

#Q1 remove kth node from the end
k=3
curr=head
n=0
while curr!=None :
    n+=1
    curr=curr.next
l=n-k+1
curr=head
for i in range(l-2):
    curr=curr.next
curr.next=curr.next.next
printlinkedlist(head)
#two pointer method
k=1
first=head
second=head
for i in range(k):
    second=second.next
if second==None :
    head=head.next
    printlinkedlist(head)
else:
    while second.next != None :
        first=first.next
        second=second.next
    first.next=first.next.next
    printlinkedlist(head)

#Q2 remove duplicates from sorted list
i=head
j=head.next
while j!=None :
    if i.num!=j.num :
        i=i.next
        j=j.next
    else:
        j=j.next
        i.next=i.next.next

printlinkedlist(head)

#second method
if head == None or head.next == None :
    printlinkedlist(head)
else:
    curr = head
    while curr.next!=None :
        if curr.num == curr.next.num :
            curr.next=curr.next.next
        else:
            curr=curr.next
    printlinkedlist(head)