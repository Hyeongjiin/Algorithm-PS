import sys
input = sys.stdin.readline

N = int(input())
orders = list(map(int, input().split()))
wait = []
current = 1

for order in orders:
  if order == current:
    current += 1
  else:
    wait.append(order)

  while wait:
    if wait[-1] == current:
      wait.pop()
      current += 1
    else:
      break

if current == N + 1:
  print("Nice")
else:
  print("Sad")