#binary search tree
#demo BST
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

a1=node(11)
a2=node(8)
a3=node(12)
a4=node(6)
a5=node(10)
a6=node(9)
a7=node(14)
a8=node(13)
a9=node(16)
a10=node(15)

a1.left=a2
a1.right=a3
a2.left=a4
a2.right=a5
a5.left=a6
a3.right=a7
a7.left=a8
a7.right=a9
a9.left=a10

root=a1

#Q (find k in BST)
k=18
if root == None :
    print(None)
curr=root
prev=None
while curr != None :
    prev=curr
    if curr.data == k :
        print("already exist")
        break
    elif curr.data > k :
        curr=curr.left
    else:
        curr=curr.right

if curr == None :
    newnode = node(k)
    if prev.data > k :
        prev.left=newnode
    else:
        prev.right=newnode
