from collections import deque
N = int(input())
queue = deque()
for i in range(N):
    queue .append(i + 1)

while queue:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
    queue.append(queue.popleft())