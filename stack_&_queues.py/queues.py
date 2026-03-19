#queue
class Queue:
    def __init__(self):
        self.q=[]
        self.front=-1
        self.length = 0
    def push(self,x):
        self.length+=1
        if self.front == -1 :
            self.front = 0
        self.q.append(x)
    def pop(self):
        self.length-=1
        if self.front == -1 :
            return -1
        if self.front == self.length :
            self.q=[]
            self.front=-1
            self.length = 0
        i=self.front
        self.front +=1
        return self.q[i]
    def getfront(self):
        if self.front == -1 :
            return -1
        return self.q[self.front]
    def size(self):
        return self.length

a = Queue()
a.push(1)
a.push(2)
a.push(3)
a.push(4)

print(a.size())
print(a.getfront())
print(a.pop())
print(a.size())


#linked list implimantation of queue
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self):
        self.rear = None
        self.back = None
        self.length = 0
    def push(self,x):
        self.length +=1
        newnode = node(x)
        if self.back == None :
            self.rear = newnode
            self.back = newnode
        else:
            self.back.next = newnode
            self.back = self.back.next
    
    def pop(self):
        self.length -= 1
        if self.rear == None :
            self.back = None
            return -1
        i = self.rear
        self.rear = self.rear.next
        return i.data
    def top(self):
        if self.rear == None :
            return -1
        return self.rear.data
    def size(self):
        return self.length


print("##########")
a = queue()
a.push(1)
a.push(2)
a.push(3)
a.push(4)

print(a.size())
print(a.top())
print(a.pop())
print(a.size())
