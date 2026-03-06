dict1={1:"a",2:"b","c":3}
print(dict1[1])
print(dict1)

#opreations
print(len(dict1))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict1[1]="z"
dict1[3]="e"
dict1.update({4:"rahul",6:"aman"})
i=dict1.pop(1)
print(i)
del dict1[6]
print(dict1.get(4))
print(dict1.get(10))
dict2=dict1.copy()
print(dict2)
dict2.clear()
print(dict2)

for key,value in dict1.items():
    print(key,value)

#question for dictionary
sentance="hello am chitti speed one terabite memory one petabite"
freq={}
for i in sentance:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
print(freq)