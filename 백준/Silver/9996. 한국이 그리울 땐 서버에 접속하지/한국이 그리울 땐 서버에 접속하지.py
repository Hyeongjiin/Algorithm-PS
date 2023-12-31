import sys

input = sys.stdin.readline

N = int(input())
stand = input().rstrip().split('*')
for _ in range(N):
  word = input().rstrip()
  if len(word) < len(stand[0]) + len(stand[1]):
    print("NE")
    continue
  if word.startswith(stand[0]) and word.endswith(stand[1]):
    print("DA")
  else:
    print("NE")