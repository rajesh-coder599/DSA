# Maximum Distance Between a Pair of Values

nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]

mx_dt=0
i=0
j=0
while i<len(nums1) and j<len(nums2) :
    if nums1[i]<=nums2[j]:
        mx_dt=max(mx_dt,j-i)
        j+=1
    else:
        i+=1
        if i>j:
            j=i
print(mx_dt)