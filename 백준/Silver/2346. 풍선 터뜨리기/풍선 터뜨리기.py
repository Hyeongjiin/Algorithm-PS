from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
balloons = list(map(int, input().split()))
q = deque()
for i in range(N):
  q.append((balloons[i], i + 1))

result = []
balloon = q.popleft()
move = balloon[0]
result.append(balloon[1])

while q:
  if move > 0:
    for i in range(move):
      q.append(q.popleft())
    balloon = q.pop()
    move = balloon[0]
    result.append(balloon[1])
  elif move < 0:
    move *= -1
    for i in range(move):
      q.appendleft(q.pop())
    balloon = q.popleft()
    move = balloon[0]
    result.append(balloon[1])

for i in result:
  print(i, end = " ")