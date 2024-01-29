import heapq

T = int(input())
for _ in range(T):
  N = int(input())
  max_q = []
  min_q = []
  count = 0
  used = [0] * N
  for i in range(N):
    operation = input().split()
    operator = operation[0]
    num = int(operation[1])
    if operator == 'I':
      heapq.heappush(min_q, (num, i))
      heapq.heappush(max_q, (-num, i))
      count += 1
    elif operator == 'D':
      if num == 1 and max_q:
        out = heapq.heappop(max_q)
        used[out[1]] = 1
      elif num == -1 and min_q:
        out = heapq.heappop(min_q)
        used[out[1]] = 1
    while max_q and used[max_q[0][1]] == 1:
      heapq.heappop(max_q)
    while min_q and used[min_q[0][1]] == 1:
      heapq.heappop(min_q)
  if not max_q:
    print("EMPTY")
  else:
    print(-heapq.heappop(max_q)[0], heapq.heappop(min_q)[0])