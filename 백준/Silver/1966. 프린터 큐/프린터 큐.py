from collections import deque

T = int(input())
for i in range(T):
  N, M = map(int, input().split())
  docu = deque()
  importance = list(map(int, input().split()))
  for j in range(N):
    docu.append((importance[j], j))
  count = 0
  while True:
    if docu[0][0] >= max(docu, key = lambda x: x[0])[0]:
      pick = docu.popleft()
      count += 1
      if (pick[1] == M):
        break
    else:
      docu.append(docu.popleft())
  print(count)