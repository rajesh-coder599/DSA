#Q1
#n-th tribonacci numbwer
def tribonacci(n):
    if n==0 :
        return 0
    elif n==1 or n==2 :
        return 1
    return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)

print(tribonacci(17))

#Q2 power of two
def ispoweroftwo(n):
    if n==1 :
        return True
    elif n%2!=0 or n<=0 :
        return False
    return ispoweroftwo(n/2)
print(ispoweroftwo(3))

#Q3 power of three
def ispowerofthree(n):
    if n==1 :
        return True
    elif n%3!=0 or n<1 :
        return False
    return ispowerofthree(n/3)
print(ispowerofthree(9))

#Q4 greatest common factor
def gcd(a,b):
    if b==0 :
        return a
    return gcd(b,a%b)
print(gcd(50,15))

#Q5 least common multiple
def lcm(a,b):
    return a*b//gcd(a,b)
print(lcm(15,50))

#Q6 x to the power n
def pow(x,n):
    if x==0 and n==0 :
        return "can not possible"
    elif n==0 :
        return 1
    elif x==0 :
        return 0
    a=pow(x,n//2)
    if n%2 == 0 and n>0:
        return a*a
    elif n%2!=0 and n>0:
        return a*a*x
x=float(input())
n=float(input())
if n>=0 :
    print(pow(x,n))
else:
    print(1/pow(x,n*(-1)))