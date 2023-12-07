import sys

input = sys.stdin.readline

N = int(input())
main = int(input())
candi = []
result = 0
for i in range(N - 1):
  candi.append(int(input()))
if N == 1:
  print(result)
else:
  while main <= max(candi):
    candi.sort(reverse=True)
    main += 1
    candi[0] -= 1
    result += 1
  print(result)