import sys

input = sys.stdin.readline

N = int(input())
stand = input().rstrip().split('*')
for _ in range(N):
  word = input().rstrip()
  if len(word) < len(stand[0]) + len(stand[1]):
    print("NE")
    continue
  flag = 0
  for i in range(len(stand[0])):
    if stand[0][i] != word[i]:
      flag = 1
      break
  if flag == 0:
    for i in range(len(stand[1])):
      if stand[1][-1 - i] != word[-1 - i]:
        flag = 1
        break
  if flag == 1:
    print("NE")
  else:
    print("DA")
