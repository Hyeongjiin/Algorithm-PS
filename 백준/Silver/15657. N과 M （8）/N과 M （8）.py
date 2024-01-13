import sys
input = sys.stdin.readline

def sequence(M, data):
  def backtrack(curr, start):
    if len(curr) == M:
      ans.append(curr[:])
      return

    for i in range(start, len(data)):
      curr.append(data[i])
      backtrack(curr, i)
      curr.pop()

  ans = []
  curr = []
  backtrack(curr, 0)
  return ans

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = sequence(M, data)
for i in result:
  print(*i)