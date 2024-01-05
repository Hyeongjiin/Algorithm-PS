import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()
start = 0 
end = len(data) - 1
mini = int(1e12)
answer = []

while start < end:
  result = data[start] + data[end]
  if abs(result) < mini:
    mini = abs(result)
    answer = [data[start], data[end]]
  if result > 0:
    end -= 1
  elif result < 0:
    start += 1
  else:
    break

print(*answer)