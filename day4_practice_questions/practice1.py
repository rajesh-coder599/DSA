#Q1 (maximum sum of subarray)
list1=[1,2,-3,4,-5]
current_sum=0
max_sum=list1[0]
for i in range(len(list1)):
    current_sum+=list1[i]
    if current_sum>max_sum:
        max_sum=current_sum
    if current_sum<0:
        current_sum=0

print(max_sum)
