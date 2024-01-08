import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
memo = {}
for i in range(N):
  memo[data[i]] = i
M = int(input())
l = list(map(int, input().split()))
for i in l:
  if i in memo:
    print(1, end = " ")
  else:
    print(0, end = " ")