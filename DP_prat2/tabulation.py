# bottom up approach

# nth fibonacci number

def fib(n):
    if n==1 or n==0 :
        return n
    n1=0
    n2=1
    for _ in range(1,n):
        temp=n2
        n2=n1+n2
        n1=temp
    return n2

print(fib(9))