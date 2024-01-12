import sys
input = sys.stdin.readline

def sequence(M, data):
  def backtrack(curr):
    if len(curr) == M:
      ans.append(curr[:])
      return

    for i in data:
      curr.append(i)
      backtrack(curr)
      curr.pop()

  ans = []
  curr = []
  backtrack(curr)
  return ans

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = sequence(M, data)
for i in result:
  print(*i)