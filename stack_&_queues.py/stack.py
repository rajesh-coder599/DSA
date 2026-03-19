#stack
class stack:
    def __init__(self):
        self.stack = []
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if len(self.stack) == 0 :
            return
        x=self.stack[-1]
        self.stack.pop()
        return x
    def top(self):
        if len(self.stack)==0 :
            return
        return self.stack[-1]
    def size(self):
        return len(self.stack)

a=stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
print(a.top())
print(a.pop())
print(a.top())
print(a.size())

#linked list implimantation of stack
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.stack = None
        self.length = 0
    def push(self,x):
        self.length +=1
        if self.stack == None :
            self.stack = x
        else:
            newnode=node(x)
            newnode.next=self.stack
            self.stack=newnode
    def top(self):
        return self.stack.data
    def pop(self):
        self.length -= 1
        if self.stack == None :
            return -1
        self.stack= self.stack.next
        return self.stack
    def size(self):
        return self.length
    
a=stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
print(a.top())
print(a.pop())
print(a.top())
print(a.size())