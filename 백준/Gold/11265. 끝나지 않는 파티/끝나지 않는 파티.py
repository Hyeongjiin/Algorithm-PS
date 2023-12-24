import sys
input = sys.stdin.readline

N, M = map(int, input().split())
party = []
for i in range(N):
  party.append(list(map(int, input().split())))

for k in range(N):
  for i in range(N):
    for j in range(N):
      party[i][j] = min(party[i][j], party[i][k] + party[k][j])

for i in range(M):
  start, end, time = map(int, input().split())
  if party[start - 1][end - 1] <= time:
    print("Enjoy other party")
  else:
    print("Stay here")