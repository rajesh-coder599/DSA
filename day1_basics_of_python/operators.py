#arithmetic operators
print(7+4)#addition
print(7-4)#subtraction
print(7/4)#division
print(7*4)#multiplication
print(7//4)#floor division
print(7**4)#7 to the power 4
print(7%4)#modulo(gives remainder)

#assignment operators
a=7
b=4#assignment operator
b+=1 #add and assign
a-=1 #subtract and assign
a*=2 #multiple and assign
#etc

#comparison operators
print(a==b)#equal to
print(a!=b)#not equal to
print(a>=b)#greater than or equal to
print(a<=b)#less than or equal to
print(a>b)#greater than
print(a<b)#less than

#logical operators
print(a>b and a==b)#both condition has to be true to return true
print(a>b or a==b)#both condition has to be false to return false
print(not a<b)#retun oposite of condition

#membership operators
str1="rajesh rayal"
print("a" in str1)#returns true if value is found
print("y" not in str1)#returns false if value is not found

#identity operators
i = 7
j = i
k = 7
print(i is j)#returns true if both variable are the same object
print(i is k)#false (because both variable ocupi diffrent memmory)
print(i is not k)#returns true if both variable are not the same object