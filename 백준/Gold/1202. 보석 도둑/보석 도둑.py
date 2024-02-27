import heapq
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
datas = []
for _ in range(N):
  w, v = map(int, input().split())
  heapq.heappush(datas, (w, v))

backpacks = []
for _ in range(K):
  backpacks.append(int(input()))

backpacks.sort()

answer = 0
possible = []
for backpack in backpacks:
  while datas and backpack >= datas[0][0]:
    v = heapq.heappop(datas)[1]
    heapq.heappush(possible, -v)
  if possible:
    answer += -heapq.heappop(possible) 

print(answer)