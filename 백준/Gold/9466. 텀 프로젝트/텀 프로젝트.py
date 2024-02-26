import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(idx):
  global answer
  visited[idx] = True
  cycle.append(idx)
  nxt_student = students[idx]
  if visited[nxt_student] == True:
    if nxt_student in cycle:
      answer -= len(cycle[cycle.index(nxt_student)::])
  else:
    dfs(nxt_student)


T = int(input())
for _ in range(T):
  N = int(input())
  answer = N
  students = [0]
  students += list(map(int, input().split()))
  visited = [False] * (N + 1)
  for idx in range(1, N + 1):
    cycle = []
    if visited[idx] == False:
      dfs(idx)
  print(answer)
