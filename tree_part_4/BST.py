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

#insert in bst
target=7
newnode=node(7)
curr=root
prev=None
while curr != None :
    prev=curr
    if curr.data == target :
        print("aready exist")
        break
    if curr.data > target :
        curr=curr.left
    if curr.data < target :
        curr=curr.right

if curr == None:
    if prev.data > target :
        prev.left = newnode
    else:
        prev.right = newnode

#Dlete in BST
def deletenode(root,target):
    if root == None :
        return None
    if root.data > target :
        root.left = deletenode(root.left,target)
    elif root.data < target :
        root.right = deletenode(root.right,target)
    else:
        if root.left == None and root.right == None :
            return None
        elif root.left == None :
            return root.right
        elif root.right == None :
            return root.left
        else:
            temp = root.right
            while temp.left != None :
                temp = temp.left
            root.data=temp.data
            root.right = deletenode(root.right,temp.data)
    return root


ans=[]
def inorder(x):
    if x is None :
        return
    inorder(x.left)
    ans.append(x.data)
    inorder(x.right)
    return ans
curr=root
print(inorder(curr))

curr=root
deletenode(curr,7)
curr=root
ans=[]
print(inorder(curr))