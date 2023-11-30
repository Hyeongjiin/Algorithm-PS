import sys
input = sys.stdin.readline
equations = input().strip().split('-')
mini = 0
count = 0
for equation in equations:
  compute = list(map(int, equation.split('+')))
  result = sum(compute)
  if count == 0:
    mini += result
    count += 1
  else:
    mini -= result

print(mini)