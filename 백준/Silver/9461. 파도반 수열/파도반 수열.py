import sys
input = sys.stdin.readline

data = [0] * 101
data[1] = 1
data[2] = 1
data[3] = 1
data[4] = 2
data[5] = 2
data[6] = 3
data[7] = 4
data[8] = 5
for i in range(9, 101):
  data[i] = data[i - 1] + data[i - 5]

T = int(input())
for i in range(T):
  N = int(input())
  print(data[N])