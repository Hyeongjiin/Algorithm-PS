import sys

def nums(code):
  result = 0
  for char in code:
    if '1' <= char <= '9':
      result += int(char)
  return result

input = sys.stdin.readline

N = int(input())
list = []
for i in range(N):
  list.append(input().rstrip())

list.sort(key=lambda x: (len(x), nums(x), x))

for i in list:
  print(i)