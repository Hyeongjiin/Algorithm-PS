import sys

input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
  data.append(tuple(map(int, input().split())))
data.append(data[0])
x = 0
y = 0
for i in range(N):
  x += data[i][0] * data[i + 1][1]
  y += data[i][1] * data[i + 1][0]

answer = round(abs(x - y) / 2, 2)
print(answer)