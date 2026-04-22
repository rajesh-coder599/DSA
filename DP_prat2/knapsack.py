# knapsack problem and it's variant

def knapsack(i,c,value,weight):
    if i==len(value):
        return 0
    take=0
    if weight[i]<=c:
        take=value[i]+knapsack(i+1,c-weight[i],value,weight)

    not_take=knapsack(i+1,c,value,weight)

    return max(take,not_take)

values=[10,5,8,5,3]
weights=[3,2,4,6,4]
c=6

ans=knapsack(0,c,values,weights)
print(ans)