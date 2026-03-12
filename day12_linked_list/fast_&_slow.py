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

fast=head
slow=head

while fast!=None and fast.next!=None :
    slow=slow.next
    fast=fast.next.next
print(slow.num)