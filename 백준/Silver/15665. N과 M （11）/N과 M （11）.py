import sys
input = sys.stdin.readline

def sequence(M, data):
  def backtrack(curr):
    if len(curr) == M:
      ans.append(curr[:])
      return 

    for i in range(len(data)):
      curr.append(data[i])
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
result = list(set(map(tuple, result)))
result.sort()
for i in result:
  print(*i)
