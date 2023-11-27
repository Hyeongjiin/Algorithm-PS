import heapq 

n = int(input())
card = []
for i in range(n):
  num = int(input())
  card.append(num)

card.sort()

result = 0
while len(card) > 1:
  A = heapq.heappop(card)
  B = heapq.heappop(card)
  total = A + B
  result += total
  heapq.heappush(card, total)

print(result)
