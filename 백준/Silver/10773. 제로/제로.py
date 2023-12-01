import sys

input = sys.stdin.readline

N = int(input())
book = []
for i in range(N):
  num = int(input())
  if num == 0:
    book.pop()
  else:
    book.append(num)
print(sum(book))