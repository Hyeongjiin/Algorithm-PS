import sys

input = sys.stdin.readline

N = int(input())
data = input().rstrip()
color = data[0]
count = 1
for i in data:
  if color != i:
    count += 1
    color = i
answer = count // 2 + 1
print(answer)