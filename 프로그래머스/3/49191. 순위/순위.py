def solution(n, results):
    if n == 1:
        return 1
    INF = int(1e9)
    distances = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        distances[i][i] = 0
    for result in results:
        distances[result[1]][result[0]] = 1
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
                
    for distance in distances:
        print(distance)
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            if distances[i][j] > 0 and distances[i][j] < INF:
                visited[i] += 1
                visited[j] += 1
    print(visited)
    answer = visited.count(n - 1)
    return answer