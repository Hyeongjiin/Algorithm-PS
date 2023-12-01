import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
  S = input().strip()
  while "()" in S:
    S = S.replace("()", "")
  if S == "":
    print("YES")
  else:
    print("NO")