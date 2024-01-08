import sys
input = sys.stdin.readline

N = int(input())
empty = 1
fill = 2
result = empty + fill
for i in range(N - 1):
  nempty = empty + fill
  nfill = empty * 2 + fill
  empty = nempty
  fill = nfill
  result = (empty + fill) % 9901 

print(result)