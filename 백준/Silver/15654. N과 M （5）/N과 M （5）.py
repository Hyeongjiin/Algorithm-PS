import sys
input = sys.stdin.readline

def permutation(data, M):
  def backtrack(curr):
    if len(curr) == M:
      ans.append(curr[:])
      return 

    for i in data:
      if i not in curr:
        curr.append(i)
        backtrack(curr)
        curr.pop()

  curr = []
  ans = []
  backtrack(curr)
  return ans

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = permutation(data, M)
for i in result:
  print(*i)