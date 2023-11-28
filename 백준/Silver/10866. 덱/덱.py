from collections import deque
import sys 

input = sys.stdin.readline

n = int(input())
q = deque()
for i in range(n):
  command = input().rstrip().split(" ")
  order = command[0]
  num = ''
  if len(command) == 2:
    num = int(command[1])
  if order == 'push_back':
    q.append(num)
  elif order == 'push_front':
    q.appendleft(num)
  elif order == 'pop_back':
    if q:
      print(q.pop())
    else:
      print(-1)
  elif order == 'pop_front':
    if q:
      print(q.popleft())
    else:
      print(-1)
  elif order == 'back':
    if q:
      print(q[-1])
    else:
      print(-1)
  elif order == 'front':
    if q:
      print(q[0])
    else:
      print(-1)
  elif order == 'size':
    print(len(q))
  elif order == 'empty':
    if q:
      print(0)
    else:
      print(1)
