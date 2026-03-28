#heap

##min heap
import heapq

h=[]
heapq.heapify(h)
heapq.heappush(h,1)
heapq.heappush(h,3)
heapq.heappush(h,5)
heapq.heappush(h,8)
heapq.heappush(h,9)
heapq.heappush(h,14)
heapq.heappush(h,19)

print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.nlargest(1,h))

#find kth largest
print(heapq.nlargest(3,h)[-1])
