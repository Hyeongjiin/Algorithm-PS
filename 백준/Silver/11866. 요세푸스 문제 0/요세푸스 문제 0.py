from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque()
for i in range(1, N + 1):
  q.append(str(i))

result = []
while q:
  for i in range(1, K):
    q.append(q.popleft())
  result.append(q.popleft())

answer = "<"
answer += ', '.join(result)
answer += ">"
print(answer)