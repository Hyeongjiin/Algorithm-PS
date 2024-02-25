from collections import deque
import sys

input = sys.stdin.readline


def bfs(idx):
  q = deque()
  q.append(idx)
  visited[idx] = True
  candy_count = candy[idx]
  friend_count = 1
  while q:
    cur_idx = q.popleft()
    for friend in friends[cur_idx]:
      if visited[friend] == False:
        candy_count += candy[friend]
        friend_count += 1
        visited[friend] = True
        q.append(friend)

  return (friend_count, candy_count)


N, M, K = map(int, input().split())
candy = [0]
candy += list(map(int, input().split()))
friends = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v = map(int, input().split())
  friends[u].append(v)
  friends[v].append(u)
visited = [False] * (N + 1)

result = []

for i in range(1, N + 1):
  if visited[i] == False:
    result.append(bfs(i))

dp = [0] * (K + 1)
for i in range(len(result)):
  friend_count, candy_count = result[i]
  for j in range(K, friend_count - 1, -1):
    dp[j] = max(dp[j - friend_count] + candy_count, dp[j])

print(dp[K - 1])
