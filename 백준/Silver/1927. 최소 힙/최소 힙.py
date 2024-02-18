import heapq 
import sys

input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
  order = int(input())
  if order == 0:
    if data:
      print(heapq.heappop(data))
    else:
      print(0)
  else:
    heapq.heappush(data, order)