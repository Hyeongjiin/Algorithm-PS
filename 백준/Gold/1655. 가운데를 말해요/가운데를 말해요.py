import heapq
import sys

input = sys.stdin.readline

maxHeap = []
minHeap = []
midian = 0

N = int(input())
for i in range(N):
  num = int(input())
  if i == 0:
    midian = num
    print(midian)
  elif i % 2 == 1:
    if num > midian:
      heapq.heappush(minHeap, num)
      print(midian)
    else:
      heapq.heappush(maxHeap, -num)
      print(-maxHeap[0])
  else:
    if num > midian:
      heapq.heappush(minHeap, num)
    else:
      heapq.heappush(maxHeap, -num)
    if len(minHeap) > len(maxHeap):
      heapq.heappush(maxHeap, -midian)
      midian = heapq.heappop(minHeap)
    elif len(minHeap) < len(maxHeap):
      heapq.heappush(minHeap, midian)
      midian = -heapq.heappop(maxHeap)
    print(midian)
