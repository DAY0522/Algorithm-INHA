# BFS를 미로 문제에 적용
from collections import deque

# n개의 행, m개의 열
n, m = map(int, input().split())

# 미로의 정보 입력
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

# 방향 정보(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS maze 구현
def bfs(x, y): # x, y는 시작점
    queue = deque()
    queue.append((x, y)) # 큐에 시작점 삽입

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i] # x: 열
            ny = y + dy[i] # y: 행
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # 아직 방문하지 않은 노드에 대해서만 최단 거리 기록
            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y]+1
    # 맨 끝까지의 최단 거리 반환
    print(maze[n-1][m-1])

# BFS 수행 결과 출력
bfs(0, 0)