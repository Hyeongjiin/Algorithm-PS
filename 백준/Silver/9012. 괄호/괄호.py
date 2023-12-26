import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
  S = input().strip()
  for i in range(30):
    S = S.replace("()", "")
  if S == "":
    print("YES")
  else:
    print("NO")