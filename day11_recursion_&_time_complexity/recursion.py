#recursion

#print 1 to n using recursion
def show(k,n,s):
    if k<=n :
        print(k)
        return show(k+s,n,s)
    else:
        return
show(1,9,2)

# factorial of n
def factorial(n):
    if n==0 :
        return 1
    return n*factorial(n-1)

print(factorial(5))

#recursive stack
def fun(n):
    if n==0 :
        return
    fun(n-1)
    print(n)
fun(8)

#recursive tree
def fibo_series(n):
    if n<=1 :
        return n
    return fibo_series(n-1) + fibo_series(n-2)
    
print(fibo_series(17))