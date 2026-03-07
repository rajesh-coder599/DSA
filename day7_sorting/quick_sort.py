#quick sort
class sort:
    def partition(self,num,l,r):
        key=num[l]
        start=l

        for i in range(l,r+1):
            if num[i]<=key :
                temp=num[i]
                num[i]=num[start]
                num[start]=temp
                start+=1
        return start-1
    def quicksort(self,num,l,r):
        if l>=r :
            return
        p = self.partition(self,num,l,r)
        self.quicksort(num,l,p-1)
        self.quicksort(num,p+1,r)
    def sortarray(self,num):
        n=len(num)
        self.quicksort(num,0,n-1)
        return num
s=sort()
print(s.sortarray([4,3,2,1]))