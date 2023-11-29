from collections import deque
import sys

input = sys.stdin.readline

S = input()
q = []
flag = 0
for i in S:
  if i == '<':
    flag += 1
    while q:
      print(q.pop(), end = "")
    print("", end = "")
    
  if flag == 0 and i != " " and i != "\n":
    q.append(i)
  if flag == 0 and i == " ":
    while q:
      print(q.pop(), end = "")
    print(" ", end = "")

  if i == '>':
    flag -= 1
    print(i, end = "")
    
  if flag == 1:
    print(i, end = "")

while q:
  print(q.pop(), end = "")