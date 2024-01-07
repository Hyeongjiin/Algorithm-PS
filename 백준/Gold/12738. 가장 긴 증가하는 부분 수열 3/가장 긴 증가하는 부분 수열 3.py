import sys

input = sys.stdin.readline
N = int(input())
INF = -int(1e10)
answer = [INF]
datas = list(map(int, input().rstrip().split()))
for data in datas:
  if data > answer[-1]:
    answer.append(data)
  else:
    start = 0
    end = len(answer)
    while start < end:
      mid = (start + end) // 2
      if answer[mid] < data:
        start = mid + 1
      else:
        end = mid
    answer[start] = data
print(len(answer) - 1)