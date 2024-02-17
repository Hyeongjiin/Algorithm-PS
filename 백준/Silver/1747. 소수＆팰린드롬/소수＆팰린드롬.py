import sys

input = sys.stdin.readline

N = int(input())
data = [True] * 2000001
for i in range(2, 2000001):
  if data[i] == True:
    j = 2
    while i * j <= 2000000:
      data[i * j] = False
      j += 1

if N > 1:
  for i in range(N, 2000001):
    if data[i] == True and str(i) == str(i)[::-1]:
        print(i)
        break
else:
  for i in range(2, 2000001):
    if data[i] == True and str(i) == str(i)[::-1]:
        print(i)
        break