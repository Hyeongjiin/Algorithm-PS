import sys

input = sys.stdin.readline
N = int(input())
INF = -int(1e10)
answer = [INF]
datas = list(map(int, input().rstrip().split()))
check = [0] * (N)
for i in range(N):
  if datas[i] > answer[-1]:
    answer.append(datas[i])
    check[i] = len(answer) - 1 
  else:
    start = 0
    end = len(answer)
    while start < end:
      mid = (start + end) // 2
      if answer[mid] < datas[i]:
        start = mid + 1
      else:
        end = mid
    check[i] = start
    answer[start] = datas[i]

result = len(answer) - 1
print(result)
answer = []
for i in range(N - 1, -1, -1):
  if check[i] == result:
    answer.append(datas[i])
    result -= 1
answer = answer[::-1]
print(*answer)