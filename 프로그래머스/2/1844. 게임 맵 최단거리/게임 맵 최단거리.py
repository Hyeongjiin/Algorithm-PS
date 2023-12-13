from collections import deque

def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    x, y = 0, 0
    q = deque([(x, y)])
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        current = q.popleft()
        x = current[0]
        y = current[1]
        if x == N - 1 and y == M - 1:
            answer = maps[N -1][M - 1]
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    if answer == 0:
        answer = -1
    return answer