import sys

input = sys.stdin.readline

N = int(input())
R = []
G = []
B = []

INF = int(1e9)

for _ in range(N):
  data = list(map(int, input().split()))
  R.append(data[::])
  G.append(data[::])
  B.append(data[::])

for i in range(3):
  if i == 0:
    R[1][i] += INF
  else:
    R[1][i] += R[0][0]

for i in range(3):
  if i == 1:
    G[1][i] += INF
  else:
    G[1][i] += G[0][1]

for i in range(3):
  if i == 2:
    B[1][i] += INF
  else:
    B[1][i] += B[0][2]

for i in range(2, N):
  R[i][0] += min(R[i-1][1], R[i-1][2])
  R[i][1] += min(R[i-1][0], R[i-1][2])
  R[i][2] += min(R[i-1][0], R[i-1][1])

for i in range(2, N):
  G[i][0] += min(G[i-1][1], G[i-1][2])
  G[i][1] += min(G[i-1][0], G[i-1][2])
  G[i][2] += min(G[i-1][0], G[i-1][1])

for i in range(2, N):
  B[i][0] += min(B[i-1][1], B[i-1][2])
  B[i][1] += min(B[i-1][0], B[i-1][2])
  B[i][2] += min(B[i-1][0], B[i-1][1])

minR = min(R[N-1][1], R[N-1][2])
minG = min(G[N-1][0], G[N-1][2])
minB = min(B[N-1][0], B[N-1][1])

answer = min(minR, minG, minB)
print(answer)