# Minimum Absolute Distance Between Mirror Pairs

nums = [12,21,45,33,54]
def mini_dis(nums):
    if len(nums)==1:
        return -1
    dic={}
    ans=-1
    for i in range(len(nums)):
        x=str(nums[i])
        y=int(x[::-1])
        if y in dic:
            if ans==-1:
                ans=abs(dic[y]-i)
            else:
                ans=min(ans,abs(dic[y]-i))
            dic[y]=i
        else:
            dic[nums[i]]=i

    return ans

print(mini_dis(nums))