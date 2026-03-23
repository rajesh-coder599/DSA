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

#hight of tree
def hight(root):
    if root == None :
        return 0
    return max(hight(root.left),hight(root.right))+1
print(hight(root))

#right look
def rightlook(root):
    ans=[]
    q=[]
    ans.append(root.data)
    q.append(root)
    while len(q)>0 :
        l=len(q)
        temp=None
        for _ in range(l):
            a=q.pop(0)
            if a.left != None :
                temp=a.left.data
                q.append(a.left)
            if a.right != None :
                temp=a.right.data
                q.append(a.right)
        if temp != None :
            ans.append(temp)
    return ans

print(rightlook(root))