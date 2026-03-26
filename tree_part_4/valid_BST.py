#valid BST
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


def validbst(root,mn,mx):
    if root == None :
        return True
    if root.data<mn or root.data>mx :
        return False
    right=validbst(root.right,root.data+1,mx)
    left=validbst(root.left,mn,root.data-1)
    return right and left

mn=0
mx=100
curr=root
print(validbst(curr,mn,mx))