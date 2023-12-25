import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()
target = int(input())
start = 0
end = N - 1
answer = 0
while start < end:
  total = data[start] + data[end]
  if total == target:
    answer += 1
    start += 1
  elif total < target:
    start += 1
  else:
    end -= 1
print(answer)