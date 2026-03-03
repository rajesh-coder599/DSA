#Q1
nums=[3,4,1,6,4]
ans=[]
for i in range(len(nums)):
    ans.append(sum(nums[:i+1]))
print(ans)

#Q2 with O(n)
num=[1,1,2,3,4,4,4,5,6,6,6,7,11]
i=0
for j in range(1,len(num)):
    if (num[i]!=num[j]):
        i+=1
        num[i]=num[j]
uniqe_number=i+1
print(uniqe_number,num)

#Q3
num1=[1,1,1,2,2,2,3,4,4,5,5,5,6,6,7,7,7,7]
i=1

for j in range(2,len(num1)):
    if(num1[j]!=num1[i-2]):
        num1[i]=num1[j]
        i+=1

print(num1)

#Q4
num2=[1,2,3,4,5,6,7,8,9,10]
index=0
for i in range(len(num2)):
    if(num2[i]%2==0):
        num2[index],num2[i]=num2[i],num2[index]
        index+=1
print(num2)

