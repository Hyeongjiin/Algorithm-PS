import sys
input = sys.stdin.readline

def sequence(data, M):
  def backtrack(curr, start):
    if len(curr) == M:
      ans.append(curr[:])
      return 

    for i in range(start, N):
      curr.append(data[i])
      backtrack(curr, i + 1)
      curr.pop()

  ans = []
  curr = []
  backtrack(curr, 0)
  return ans

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
result = sequence(data, M)
result = list(set(map(tuple, result)))
result.sort()
for i in result:
  print(*i)
