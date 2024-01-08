import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
d = {}
for i in data:
  d[i] = 0
M = int(input())
l = list(map(int, input().split()))
for i in l:
  if i in d:
    print(1)
  else:
    print(0)