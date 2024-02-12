import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
  word = list(input().rstrip())
  l = 0
  r = len(word) - 1
  value = 0
  while l < r:
    if word[l] == word[r]:
      l += 1
      r -= 1
    else:
      nword1 = word[::]
      nword1[l] = ""
      nword2 = word[::]
      nword2[r] = ""
      word1 = ''.join(nword1)
      word2 = ''.join(nword2)
      if word1 == word1[::-1] or word2 == word2[::-1]:
        value = 1
      else:
        value = 2
      break

  print(value)