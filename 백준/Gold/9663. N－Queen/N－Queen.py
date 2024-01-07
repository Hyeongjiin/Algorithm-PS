N = int(input())

ans = 0
pos = [0] * N

def check(idx):
  for i in range(idx):
    if pos[idx] == pos[i] or abs(pos[idx] - pos[i]) == abs(idx - i):
      return 
  return True

def queen(Q):
  global ans
  if Q == N:
    ans += 1
    return 
  else:
    for i in range(N):
      pos[Q] = i
      if check(Q):
        queen(Q + 1)

queen(0)
print(ans)