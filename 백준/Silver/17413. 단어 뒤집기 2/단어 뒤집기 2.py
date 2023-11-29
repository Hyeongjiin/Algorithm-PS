from collections import deque
import sys

input = sys.stdin.readline

S = input().rstrip()
S = S.replace('<', 'X<').replace('>', '>X').split('X')
result = ""
for i in S:
  if '<' in i:
    result += i
  else:
    words = i.split(' ')
    words = [word[::-1] for word in words]
    result += ' '.join(words)

print(result)