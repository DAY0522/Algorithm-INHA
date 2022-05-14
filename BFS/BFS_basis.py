# 큐 구현을 위한 deque 라이브러리 활용
from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    queue = deque([start])
    # 시작 노드를 방문 처리
    visited[start] = True

    # 큐가 완전히 빌 때까지 반복
    while queue:
        # 큐에서 원소 하나를 pop
        v = queue.popleft()
        print(v, end=' ')
        # pop한 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph=[
    [], # 0번 노드 비우기
    [2, 3, 8], # 1번 노드와 연결된 2, 3, 8 노드
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 정보 저장할 리스트
visited = [False]*(8+1) # (총 노드의 개수 + 인덱스 0 저장) 크기로 선언

# bfs 실행
bfs(graph, 1, visited)