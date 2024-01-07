def permutation(num, target):
  def backtrack(curr):
    if len(curr) == target:
      print(*curr)
      return
      
    for i in range(1, num + 1):
      curr.append(i)
      backtrack(curr)
      curr.pop()
  curr = []
  backtrack(curr)
  
N, M = map(int, input().split())
permutation(N, M)
