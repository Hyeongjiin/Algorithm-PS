import sys
input = sys.stdin.readline

while True:
  S = input()
  if S[0] == ".":
    break
  S = S.replace('(', 'X(X')
  S = S.replace(')', 'X)X')
  S = S.replace('[', 'X[X')
  S = S.replace(']', 'X]X')
  S = S.split('X')
  s = []
  for i in S:
    if i == '(' or i == ')' or i == '[' or i == ']':
      s.append(i)
  ns = ''.join(s)
  while '()' in ns or '[]' in ns:
    ns = ns.replace('()', '')
    ns = ns.replace('[]', '')
  if ns == '':
    print("yes")
  else:
    print("no")