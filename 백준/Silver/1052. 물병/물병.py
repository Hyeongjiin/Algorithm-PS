import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bottles = [0] * 31
bottles[0] = N
answer = 0

for i in range(1, 31):
  if bottles[i - 1] > 0:
    bottles[i] = bottles[i - 1] // 2
    bottles[i - 1] = bottles[i - 1] % 2
total = sum(bottles)
flag = 0
while total > K:
  F = -1
  S = -1
  i = 0
  while F == -1 or S == -1:
    if bottles[i] == 1:
      if F == -1:
        F = i
      else:
        S = i
    i += 1
    if i > 30:
      flag = 1
      break
  for j in range(F, S):
    answer += 2 ** j
  bottles[F] = 0
  bottles[S] = 0
  bottles[S + 1] += 1
  total -= 1
  for j in range(S + 1, 31):
    if bottles[j] == 2:
      bottles[j] = 0
      bottles[j + 1] += 1
      total -= 1
  if flag == 1:
    break

print(answer)