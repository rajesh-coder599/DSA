#demo tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

a1=node(1)
a2=node(2)
a3=node(3)
a4=node(4)
a5=node(5)
a6=node(6)
a7=node(7)
a8=node(8)
a9=node(9)
a10=node(10)

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

#preorder traversal
ans=[]
def preorder(x):

    if x == None :
        return
    ans.append(x.data)
    preorder(x.left)
    preorder(x.right)
    return ans

a=preorder(root)
print(a)

#postorder traversal
ans=[]
def postorder(x):
    if x is None :
        return
    postorder(x.left)
    postorder(x.right)
    ans.append(x.data)
    return ans

print(postorder(root))

#inorder traversal
ans=[]
def inorder(x):
    if x is None :
        return
    inorder(x.left)
    ans.append(x.data)
    inorder(x.right)
    return ans

print(inorder(root))