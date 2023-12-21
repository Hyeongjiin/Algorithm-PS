import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

start = 1
end = 20000000

result = 0
while start <= end:
  total = 0
  count = 1
  mid = (start + end) // 2
  if max(lectures) > mid:
    start = mid + 1
    continue
  for i in lectures:
    total += i
    if total > mid:
      count += 1
      total = i
  if count > M:
    start = mid + 1
  else:
    end = mid - 1
    result = mid
print(result)