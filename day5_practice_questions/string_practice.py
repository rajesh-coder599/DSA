#Q1
str1="1.1.1.1"
output_str=""
for i in str1:
    if i=="." :
        output_str+="[.]"

    else:
        output_str+=i
print(output_str)
#with replace function
print(str1.replace(".","[.]"))

#Q2
str2="A man, a plan, a canal: Panama"
alphabets=""
words="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(str2)):
    if(str2[i] in words):
        alphabets+=str2[i].lower()
if (alphabets[::-1]==alphabets):
    print("true")
else:
    print("false")

#Q3
s=["a","b","c","d"]
s.reverse()
print(s)
#with loop
a=[]
for i in range(len(s)-1,-1,-1):
    a.append(s[i])
print(a)
#with two pointer
i=0
j=len(s)-1
while i<j:
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
    i+=1
    j-=1
print(s)

#Q4
str3="   my name   is  rajesh    "
str3=(str3.strip()).split()
str3.reverse()
print(" ".join(str3))

#Q5
s1="    fly me  to  the moon  "
s1=(s1.strip()).split()
print(len(s1[-1]))
