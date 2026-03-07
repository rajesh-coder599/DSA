#merge sort
class sort:
    def merge(self,num,l,mid,r):
        a=[]
        b=[]
        for x in range(l,mid+1):
            a.append(num[x])
        for y in range(mid+1,r+1):
            b.append(num[y])
        i=0
        j=0
        k=l
        while k<=r:
            if i == len(a) :
                num[k]=b[j]
                k+=1
                j+=1
            elif j == len(b) :
                num[k]=a[i]
                k+=1
                i+=1
            elif a[i]<b[j] :
                num[k]=a[i]
                k+=1
                i+=1
            else:
                num[k]=b[j]
                k+=1
                j+=1
    def mergesort(self,num,l,r):
        if l>=r :
            return
        mid=(l+r)//2
        self.mergesort(num,l,mid)
        self.mergesort(num,mid+1,r)

        self.merge(num,l,mid,r)
    def sortarray(self,num):
        self.mergesort(num,0,len(num)-1)
        return num

s1=sort()
print(s1.sortarray([6,5,4,3,2,1]))