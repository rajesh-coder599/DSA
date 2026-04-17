#Q1
list1=[]
a=int(input("enter a number: "))
for i in range(1,a+1):
    if(i%15==0):
        list1.append("FizzBuzz")
    elif(i%3==0):
        list1.append("Fizz")
    elif(i%5==0):
        list1.append("Buzz")
    else:
        list1.append(i)

print(list1)

#Q2
start = int(input("from "))
end = int(input("to "))
count = 0
for i in range(start,end+1):
    if(i%2!=0):
        count+=1

print(count)

#Q3
def finder(a):
    list2=[]
    for i in a:
        count1=0
        for j in a:
            if(i>j):
                count1 += 1
        list2.append(count1)
    return print(list2)

finder([8,1,2,2,3])