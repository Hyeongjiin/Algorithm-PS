import sys

input = sys.stdin.readline


def colorC(x, y, size):
  global white
  global blue
  color = paper[x][y]
  flag = 0
  for i in range(x, x + size):
    if flag == 1:
      break
    for j in range(y, y + size):
      if paper[i][j] != color:
        flag = 1

  if flag == 0:
    if color == 0:
      white += 1
    elif color == 1:
      blue += 1
  else:
    nSize = size // 2
    colorC(x, y, nSize)
    colorC(x + nSize, y, nSize)
    colorC(x, y + nSize, nSize)
    colorC(x + nSize, y + nSize, nSize)


N = int(input())
paper = []
white = 0
blue = 0

for _ in range(N):
  paper.append(list(map(int, input().split())))

colorC(0, 0, N)
print(white)
print(blue)