import sys

input = sys.stdin.readline


def quad(x, y, scale, datas):
  flag = 0
  base = datas[x][y]
  for i in range(scale):
    if flag == 1:
      break
    for j in range(scale):
      if datas[x + i][y + j] != base:
        flag = 1
        break
  if flag == 0:
    print(base, end="")
  else:
    scale //= 2
    print("(", end="")
    quad(x, y, scale, datas)
    quad(x, y + scale, scale, datas)
    quad(x + scale, y, scale, datas)
    quad(x + scale, y + scale, scale, datas)
    print(")", end="")


N = int(input())
datas = []
for _ in range(N):
  datas.append(list(map(int, input().rstrip())))

quad(0, 0, N, datas)