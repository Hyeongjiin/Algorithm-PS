import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))
a = []

while queue:
  idx, num = queue.popleft()
  a.append(str(idx))
  if num > 0:
    queue.rotate(-(num-1))
  else:
    queue.rotate(-num)

print(' '.join(a))