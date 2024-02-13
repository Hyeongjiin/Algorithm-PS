def permutation(num, target):
  def backtrack(curr, start):
    if len(curr) == target:
      print(*curr)
      return
      
    for i in range(start, num + 1):
      if i not in curr:
        curr.append(i)
        backtrack(curr, i + 1)
        curr.pop()
  curr = []
  backtrack(curr, 1)
  
N, M = map(int, input().split())
permutation(N, M)
