import sys
n = int(sys.stdin.readline())

for _ in range(n):
  s = list(sys.stdin.readline().strip())
  a=[]
  for i in s:
    a.append(i)
    if i == ')':
      if len(a)==1:
        break
      a.pop()
      a.pop()
  if len(a)!=0:
    print('NO')
  else:
    print('YES')