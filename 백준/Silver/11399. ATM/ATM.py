n = int(input())
time = list(map(int, input().split()))
time.sort()
result = time[0]
for i in range(1, n):
  time[i] += time[i - 1]
  result += time[i]
print(result)