from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
list = []
for i in range(N):
  num = tuple(map(int, input().split()))
  list.append(num)

list.sort(key = lambda x : (x[0], x[1]))
for i in list:
  print(i[0], i[1])