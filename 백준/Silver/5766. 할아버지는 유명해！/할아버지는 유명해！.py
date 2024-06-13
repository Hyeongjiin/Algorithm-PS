while True:
  N, M = map(int, input().split())
  if N == 0 and M == 0:
    break
  players = [0] * 10001
  for i in range(N):
    data = list(map(int, input().split()))
    for info in data:
      players[info] += 1
  num = list(set(sorted(players)))
  num.sort(reverse=True)
  second = num[1]
  answer = []
  for i in range(1, 10001):
    if players[i] == second:
      answer.append(i)
  print(*answer)