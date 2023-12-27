import sys
input = sys.stdin.readline

def preorder(start):
  print(start, end = '')
  if tree[start][0] != '.':
    preorder(tree[start][0])
  if tree[start][1] != '.':
    preorder(tree[start][1])

def inorder(start):
  if tree[start][0] != '.':
    inorder(tree[start][0])
  print(start, end = '')
  if tree[start][1] != '.':
    inorder(tree[start][1])

def postorder(start):
  if tree[start][0] != '.':
    postorder(tree[start][0])
  if tree[start][1] != '.':
    postorder(tree[start][1])
  print(start, end = '')

N = int(input())
tree = {}
for i in range(N):
  root, left, right = input().split()
  tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')