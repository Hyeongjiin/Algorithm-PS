import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for i in range(N + M):
  name = input().rstrip()
  if name in dic:
    dic[name] += 1
  else:
    dic[name] = 1

answer = []

count = 0
for i in dic.items():
  if i[1] > 1:
    answer.append(i[0])
    count += 1

answer.sort()
print(count)
for i in answer:
  print(i)