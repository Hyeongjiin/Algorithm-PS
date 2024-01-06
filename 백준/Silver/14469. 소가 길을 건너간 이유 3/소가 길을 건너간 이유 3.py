import sys

input = sys.stdin.readline

N = int(input())
datas = []
for i in range(N):
  arrive, wait = map(int, input().split())
  datas.append((arrive, wait))
datas.sort(key = lambda x : (x[0], x[1]))
result = 0
for data in datas:
  if result < data[0]:
    result = data[0]
  result += data[1]
print(result)
