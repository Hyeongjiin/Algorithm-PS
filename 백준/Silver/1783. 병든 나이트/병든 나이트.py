N, M = map(int, input().split())

x = 0
y = 0

result = 0
if N >= 3 and M >= 7:
  x = 1
  y = 7
  result = (M - 7 + 1) + 4 
else:
  if N >= 3:
    result = M
  elif N == 2:
    result = (M - 1) // 2 + 1  
  if result > 4:
    result = 4
  if N == 1:
    result = 1
print(result)