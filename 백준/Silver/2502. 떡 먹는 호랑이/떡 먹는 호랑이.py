import sys

input = sys.stdin.readline

D, K = map(int, input().split())
data = [0] * 31
data[0] = 0
data[1] = 0
data[2] = 1
for i in range(3, 31):
  data[i] = data[i - 1] + data[i - 2]

firstDay = data[D - 1]
secondDay = data[D]

flag = 0
for i in range(1, 100000):
  if flag == 1:
    break
  count = firstDay * i
  if count > K:
    continue
  for j in range(i, 100000):
    if count > K:
      break
    if count + secondDay * j == K:
      print(i)
      print(j)
      flag = 1