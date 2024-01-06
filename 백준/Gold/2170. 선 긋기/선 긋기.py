import sys
input = sys.stdin.readline
N = int(input())
datas = []
for i in range(N):
  start, end = map(int, input().split())
  datas.append((start, end))
datas.sort(key = lambda x : (x[0], x[1]))
result = 0
start = 0 
end = 0
for data in datas:
  if start <= data[0] <= end:
    if data[1] > end:
      end = data[1]
  else:
    result += end - start
    start = data[0]
    end = data[1]
result += end - start
print(result)