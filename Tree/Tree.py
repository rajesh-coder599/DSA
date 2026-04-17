#binary tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.right.right=node(5)
root.left.left.left=node(7)
root.left.left.right=node(6)
curr=root
while curr != None :
    print(curr.data)
    curr=curr.left

