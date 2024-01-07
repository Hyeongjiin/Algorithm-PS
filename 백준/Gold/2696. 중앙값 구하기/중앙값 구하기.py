import sys
import bisect

input = sys.stdin.readline


def check(data):
  ans = [data[0]]
  order = [data[0]]
  for i in range(1, len(data)):
    bisect.insort(order, data[i])
    if i % 2 == 0:
      ans.append(order[i // 2])
  print(len(ans))
  for i in range(len(ans)):
    if i % 10 == 0 and i > 0:
      print()
    print(ans[i], end = " ")
  print()

T = int(input())
for _ in range(T):
  N = int(input())
  datas = []
  count = 0
  count += N // 10
  if N % 10 != 0:
    count += 1
  for i in range(count):
    tmp = list(map(int, input().split()))
    for i in tmp:
      datas.append(i)
  check(datas)