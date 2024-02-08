import sys
input = sys.stdin.readline
N = int(input())
data = []
width = []
height = []
cur_p = (0, 0)
data.append(cur_p)
for i in range(6):
  dir, dist = map(int, input().split())
  if dir == 4:
    cur_p = (cur_p[0], cur_p[1] + dist)
  elif dir == 3:
    cur_p = (cur_p[0], cur_p[1] - dist)
  elif dir == 2:
    cur_p = (cur_p[0] - dist, cur_p[1])
  elif dir == 1:
    cur_p = (cur_p[0] + dist, cur_p[1])
  if i != 5:
    data.append(cur_p)
    width.append(cur_p[0])
    height.append(cur_p[1])
width.sort()
height.sort()
possible = [(width[0], height[0]), (width[0], height[-1]), (width[-1], height[0]), (width[-1], height[-1])]

total = abs(width[0] - width[-1]) * abs(height[0] - height[-1])
for i in possible:
  if i not in data:
    total -= abs(width[2] - i[0]) * abs(height[2] - i[1])
print(total * N)