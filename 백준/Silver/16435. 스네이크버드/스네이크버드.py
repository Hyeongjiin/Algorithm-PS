import sys

input = sys.stdin.readline

N, L = map(int, input().split())
f = list(map(int, input().split()))
f.sort()

for i in f:
  if L >= i:
    L += 1
  else:
    break
print(L)