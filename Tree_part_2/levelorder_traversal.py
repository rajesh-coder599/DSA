#tree
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

#Queue
class queue:
    def __init__(self):
        self.q=[]
        self.rear=-1
        self.length=0
    def push(self,x):
        self.length+=1
        if self.rear == -1 :
            self.rear=0
        self.q.append(x)
    def pop(self):
        self.length-=1
        if self.rear == -1 :
            return
        k=self.q.pop(self.rear)
        if self.length == 0 :
            self.rear = -1
        return k
    def size(self):
        return self.length
    
#levelorder traversal
def levelorder(root):
    ans=[]
    if root == None :
        return ans
    q=queue()
    q.push(root)
    ans.append([root.data])
    while q.size() > 0 :
        l=q.size()
        temp=[]
        for _ in range(l):
            a=q.pop()
            if a.left != None :
                q.push(a.left)
                temp.append(a.left.data)
            if a.right != None :
                q.push(a.right)
                temp.append(a.right.data)
        if len(temp)>0 :
            ans.append(temp)

    return ans

print(levelorder(root))


 