import sys
input = sys.stdin.readline

def sequence(num, target):
  def backtrack(curr):
    if len(curr) == target:
      ans.append(curr[:])
    else:
      for i in range(1, num + 1):
        if i not in curr:
          curr.append(i)
          backtrack(curr)
          curr.pop()
  ans = []
  backtrack([])
  return ans

N, M = map(int, input().split())
result = sequence(N, M)
for i in result:
  print(*i)