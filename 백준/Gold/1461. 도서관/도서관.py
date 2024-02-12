import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))
books.sort()
left = []
right = []

for book in books:
  if book < 0:
    left.append(book)
  elif book > 0:
    right.append(book)
right.sort(reverse=True)

result = []
for i in range(0, len(left), M):
  result.append(-left[i])
  
for i in range(0, len(right), M):
  result.append(right[i])
result.sort()

answer = 0
for i in range(len(result)):
  if i == len(result) - 1:
    answer += result[i]
  else:
    answer += result[i] * 2
print(answer)
  