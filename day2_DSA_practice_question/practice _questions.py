#Q1
num1=1248
str1=str(num1)
c=0
for i in str1:
    if(num1%int(i)==0):
        c+=1
print(c)
#with while loop
c1=0
while num1>0:
    r=num1%10
    if(num1%r==0):
        c1+=1
    num1=num1//10
print(c1)

#Q2
x=121
x1=x
x2=0
while x1>0:
    p=x1%10
    x2=(x2*10+p)
    x1//=10

if(x==x2):
    print("true")
else:
    print("false")
#converting to function
def ispalindrome(a):

    x1=a
    x2=0
    while x1>0:
        p=x1%10
        x2=(x2*10+p)
        x1//=10

    if(x==x2):
        print("true")
    else:
        print("false")
ispalindrome(121)

#Q3
def sub_prod_sum(n):
    n1=n
    product=1
    digit_sum=0
    while n1>0:
        r1=n1%10
        product*=r1
        digit_sum+=r1
        n1//=10
    return product-digit_sum
ans = sub_prod_sum(345)
print(ans)

#Q4
candies=[2,6,3,1,8,0,5]
extracandies=2
boolean=[]
for i in candies:
    if(i+extracandies)>=max(candies):
        boolean.append("true")
    else:
        boolean.append("false")
print(boolean)