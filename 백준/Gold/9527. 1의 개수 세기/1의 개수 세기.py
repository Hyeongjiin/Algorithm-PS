A, B = map(int, input().split())
answer = 0
lenA = len(bin(A)) - 2
lenB = len(bin(B)) - 2
countA = 0
countB = 0

A -= 1
for i in range(1, lenA + 1):
  countA += ((A + 1) // (2 ** i)) * (2 ** (i - 1))
  rest = ((A + 1) % (2 ** i)) - (2 ** (i - 1))
  if rest > 0:
    countA += rest

for i in range(1, lenB + 1):
  countB += ((B + 1) // (2 ** i)) * (2 ** (i - 1))
  rest = ((B + 1) % (2 ** i)) - (2 ** (i - 1))
  if rest > 0:
    countB += rest

print(countB - countA)