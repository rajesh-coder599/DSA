#Q1 (Best time to buy & sell stock)
prices=[7,1,5,3,6,4]
buy=prices[0]
max_profit=0
for i in range(1,len(prices)):
    current_profit=prices[i]-buy
    if(current_profit>max_profit):
        max_profit=current_profit
    if current_profit<0:
        buy=prices[i]

print(max_profit)

#Q1 part 2
prices=[7,1,5,3,6,4]
buy=prices[0]
profit=0
for i in range(1,len(prices)):
    if prices[i]>buy:
        profit+=prices[i]-buy
        buy=prices[i]
    buy=min(prices[i],buy)
print(profit)

#Q2 (matrix)
accounts=[[1,2,3],[3,2,1]]
maximum_sum=0
for i in range(len(accounts)):
    maximum_sum = max(maximum_sum,sum(accounts[i]))

print(maximum_sum)

#Q3
matrix=[[1,2,3,4],[4,8,9,7],[4,1,0,7],[1,1,1,1]]
row=len(matrix)
col=len(matrix[0])
final_matrix=[]
el=row*col
rowstart=0
colstart=0
rowend=row-1
colend=col-1
while el>0:
    for i in range(colstart,colend+1):
        final_matrix.append(matrix[rowstart][i])
        el-=1
    rowstart+=1
    if el==0:
        break
    for i in range(rowstart,rowend+1):
        final_matrix.append(matrix[i][colend])
        el-=1
    colend-=1
    if el==0:
        break
    for i in range(colend,colstart-1,-1):
        final_matrix.append(matrix[rowend][i])
        el-=1
    rowend-=1
    if el==0:
        break
    for i in range(rowend,rowstart-1,-1):
        final_matrix.append(matrix[i][colstart])
        el-=1
    colstart+=1
    if el==0:
        break
print(final_matrix)
