#linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(1)
b=node(1)
z=node(3)
d=node(4)
e=node(5)
f=node(5)
g=node(6)

a.next=b
b.next=z
z.next=d
d.next=e
e.next=f
f.next=g

head=a

def printlinkedlist(head):
    curr=head
    while curr!=None :
        print(curr.data,end=" ")
        curr=curr.next
    print()

printlinkedlist(head)

#Q1 remove duplicates from sorted list
first=head
second=head
while second.next!=None :
    if second.data == second.next.data and second.data != second.next.next.data  :
        second.next=second.next.next
    elif second.data == second.next.data :
        second.next=second.next.next
    else:
        first=first.next
        second=second.next
printlinkedlist(head)

#Q2 reverse linked list
nxt=None
prev=None
curr=head
while curr != None :
    nxt=curr.next
    curr.next=prev
    prev=curr
    curr=nxt
head = prev
printlinkedlist(prev)

#Q3 rotate linked list k time in right
k=2

second=head
l=1
while second.next !=None :
    l+=1
    second=second.next


k=k%l
first=head
for i in range(l-k-1):
    first=first.next
second.next=head
head=first.next
first.next=None
printlinkedlist(head)

#Q4 intersaction of two linked list
class node1:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node1(7)
b=node1(10)
y=node1(8)
d=node1(9)
e=node1(1)

a.next=b
b.next=y
y.next=d
d.next=e
e.next=z

head2=a

p1=head
p2=head2
count=0
while p1 != p2 :
    p1=p1.next
    p2=p2.next
    if (p1==None):
        count+=1
        p1=head2
    if p2==None :
        p2=head
    if count>1 :
        print("null")
        break
print(p2.data)

#Q5 add two linked list

curr1=head
curr2=head2
c=0
ans=node(-1)
curr3=ans
while curr1 != None or curr2 != None :
    total=c
    c=0
    if curr1 != None :
        total+=curr1.data
        curr1=curr1.next
    if curr2 != None :
        total+=curr2.data
        curr2=curr2.next
    if total > 9 :
        c=1
        total-=10
    newnode=node(total)
    curr3.next=newnode
    curr3=curr3.next
if c>0 :
    newnode=node(c)
    curr3.next=newnode
    curr3=curr3.next

printlinkedlist(ans.next)

#Q6 linked list cycle
a=node(2)
b=node(3)
c=node(5)
d=node(7)
e=node(8)
f=node(9)

a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=c

head = a

slow = head
fast = head

while True :
    slow=slow.next
    fast=fast.next.next
    if slow == fast :
        print(True)
        break
    if fast != None and fast.next != None :
        print(False)
        break

#Q7 linked list cycle part2
slow = head
fast = head
ans=False
while fast != None and fast.next != None :
    slow=slow.next
    fast=fast.next.next
    if slow == fast :
        ans=True
        break
if not ans :
    print("null")
else:
    slow=head
    while slow != fast :
        slow=slow.next
        fast=fast.next
    print(slow.data)