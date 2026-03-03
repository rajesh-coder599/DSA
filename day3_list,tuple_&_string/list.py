#operations in list
list1=[1,2,3,4,5]
print(len(list1)) #length of list
print(list1[0]) # indexing in list
print(list1[-1]) # negative indexing
list1.append("rajesh") # add an single element(at last)
print(list1)
list1.extend("rayal") # add elvery elemen of itrable(at last)
print(list1)
list1.insert(3,100) #add an element at specific index(index,element)
print(list1)
list1.remove(list1[0]) #remove an specific element
print(list1)
x=list1.pop(3) # removes an specific index & assign a value to variable
print(x)
list1.clear() # removes all the elements from list
print(list1)


#functions in list
list2=[1,2,3,4,5,6,2,3,6,3,2,7]
print(max(list2)) # max of list
print(min(list2)) # min of list
print(list2.count(2)) # how many times occur
list2.reverse() # reverse the list
print(list2)
list2.sort() # increasing order list
print(list2)
list2.sort(reverse=True) # dicreasing order list
print(list2)
print(list2.index(7)) # gives index of first time occurence of element
list3 = list2.copy() # shalow copy
print(list2,id(list2))
print(list3,id(list3))



#slicing (this works just like range function)
list4=[34,786,4,3,78,65,44,54,66]
print(list4[1:5]) # from index 1 to 4
print(list4[:6]) # from start to 5
print(list4[::2]) #from start to end with step size of 2
print(list4[8:2:-1]) # from index 8 to 3 with step size of -1