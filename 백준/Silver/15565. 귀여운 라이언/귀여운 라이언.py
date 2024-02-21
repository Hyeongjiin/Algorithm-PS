from collections import deque
import sys

inpur = sys.stdin.readline
INF = int(1e9)

N, K = map(int, input().split())
data = list(map(int, input().split()))

q = deque()
countOne = 0
min_len = INF
for i in data:
  if i == 1:
    countOne += 1
  q.append(i)
  if countOne == K:
    while q[0] != 1:
      q.popleft()
    min_len = min(min_len, len(q))
    q.popleft()
    countOne -= 1
    while q[0] != 1:
      q.popleft()

if min_len == INF:
  min_len = -1
print(min_len)