import sys
input = sys.stdin.readline
N, M = map(int, input().split())
datas = []
for i in range(M):
  datas.append(int(input()))

start = 1
end = max(datas)
result = int(10e10)

while start <= end:
  mid = (start + end) // 2
  count = 0
  for data in datas:
    count += data // mid
    if data % mid != 0:
      count += 1
  if count > N:
    start = mid + 1
  else:
    result = min(mid, result)
    end = mid - 1
    
print(result)