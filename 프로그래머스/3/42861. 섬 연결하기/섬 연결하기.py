def solution(n, costs):
    answer = 0
    parent = [0] * n
    costs.sort(key = lambda x : x[2])
    for i in range(1, n):
        parent[i] = i
    for cost in costs:
        if find_parent(parent, cost[0]) != find_parent(parent, cost[1]):
            union_parent(parent, cost[0], cost[1])
            answer += cost[2]
    return answer

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x != y:
        parent[y] = x
        