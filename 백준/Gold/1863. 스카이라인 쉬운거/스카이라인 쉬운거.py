import sys

sys = sys.stdin.readline

N = int(input())
h = []
answer = 0
for _ in range(N):
  _, data = map(int, input().split())
  if data == 0:
    answer += len(h)
    h = []
  else:
    if not h:
      h.append(data)
    else:
      while h and h[-1] > data:
        h.pop()
        answer += 1
      if not h:
        h.append(data)
      else:
        if h[-1] < data:
          h.append(data)

if h:
  answer += len(h)

print(answer)