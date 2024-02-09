from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
  P = input()
  N = int(input())
  info = input().rstrip()
  info = info.strip("[]").split(",")
  data = deque()
  for i in info:
    data.append(i)
  left = True
  error = False
  for i in P:
    if i == 'R':
      left = not left
    elif i == 'D':
      if not data:
        print('error')
        error = True
        break
      else:
        if left:
          out = data.popleft()
          if out == '':
            print('error')
            error = True
            break
        else:
          out = data.pop()
          if out == '':
            print('error')
            error = True
            break

  if not error:
    result = "["
    if data and left:
      result += str(data[0])
      for i in range(1, len(data)):
        result += ','
        result += str(data[i])
    elif data and not left:
      result += str(data[-1])
      for i in range(len(data) - 2, -1, -1):
        result += ','
        result += str(data[i])
    result += ']'
    print(result)
