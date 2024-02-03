from collections import deque

def solution(maps):
    width = len(maps[0])
    height = len(maps)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * width for _ in range(height)]
    answer = bfs(maps, visited, width, height, moves, 0, 0)
    return answer


def bfs(maps, visited, width, height, moves, x, y):
    q = deque()
    count = 1
    q.append((x, y, count))
    visited[x][y] = True
    while q:
        cur_x, cur_y, cur_count = q.popleft()
        if cur_x == height - 1 and cur_y == width - 1:
            return cur_count
        for move in moves:
            nx = cur_x + move[0]
            ny = cur_y + move[1]
            if nx < 0 or nx > height - 1 or ny < 0 or ny > width - 1:
                continue
            if maps[nx][ny] == 0:
                continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny, cur_count + 1))
    return -1