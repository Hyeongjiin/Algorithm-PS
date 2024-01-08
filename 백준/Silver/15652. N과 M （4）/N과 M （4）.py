import sys
input = sys.stdin.readline

def sequence(N, M):
  def backtrack(curr, start):
    if len(curr) == M:
      ans.append(curr[:])
      return 

    for i in range(start, N + 1):
      curr.append(i)
      backtrack(curr, i)
      curr.pop()

  ans = []
  curr = []
  backtrack(curr, 1)
  return ans

N, M = map(int, input().split())
ans = sequence(N, M)
for i in ans:
  print(*i)