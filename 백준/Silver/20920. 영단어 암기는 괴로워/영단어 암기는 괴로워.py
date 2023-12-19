import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}
for i in range(N):
  word = input().rstrip()
  if len(word) >= M:
    if word in dict:
      dict[word] += 1
    else:
      dict[word] = 1

dict = list(dict.items())
dict.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in dict:
  print(i[0])