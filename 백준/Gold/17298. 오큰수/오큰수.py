import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
stack = []
answer = [0] * N
for idx, val in enumerate(data):
  while stack and stack[-1][1] < val:
    index, _ = stack.pop()
    answer[index] = val
  stack.append((idx, val))
while stack:
  index, _ = stack.pop()
  answer[index] = -1

answer = ' '.join(map(str, answer))
print(answer)