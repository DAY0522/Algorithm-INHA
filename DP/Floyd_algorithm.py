def floyd(W, D, P):
    n = len(W) - 1
    for i in range(1, n+1): # 초기값 설정
        for j in range(1, n+1):
            D[i][j] = W[i][j]

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if D[i][k] + D[k][j] < D[i][j]: # i에서 j를 바로 가는 것보다 k를 거쳐가는 게 더 최소인 경우
                    P[i][j] = k # 최소가 될 때의 k값 저장
                    D[i][j] = D[i][k] + D[k][j] # 최소값 저장

def path(P, q, r): # q에서 r로 가는 최단경로 상의 정점 출력
    if P[q][r] != 0:
        path(P, q, P[q][r])
        print(f'V{P[q][r]}', end=' → ')
        path(P, P[q][r], r)

def print_list(l): # list 출력
    for i in range(1, len(l)):
        for j in range(1, len(l)):
            print(f'{l[i][j]}', end=' ')
        print()
    print()

# Weight 행렬 선언
# 행과 열은 각각 노드 번호를 뜻하므로 1에서부터 시작하도록 함
# 따라서 0번째 행, 열은 무의미(각 노드 번호를 list와 맞춰주기 위함)
# 즉, n개의 노드일 때 배열은 (n+1)X(n+1) 행렬
# 무한대의 값은 파이썬의 inf(어떤 숫자와 비교해도 무조건 크다고 판정)를 이용해줌
W = [[0, 0, 0, 0, 0, 0],
     [0, 0, 1, float('inf'), 1, 5],
     [0, 9, 0, 3, 2, float('inf')],
     [0, float('inf'), float('inf'), 0, 4, float('inf')],
     [0, float('inf'), float('inf'), 2, 0, 3],
     [0, 3, float('inf'), float('inf'), float('inf'), 0]]

# P, D 행렬 선언(W와 크기 동일)
P = [[0 for _ in range(6)] for _ in range(6)]
D = [[0 for _ in range(6)] for _ in range(6)]

floyd(W, D, P) # Floyd's 알고리즘 실행

print('W[i][j] is')
print_list(W)
print('D[i][j] is')
print_list(D)
print('P[i][j] is')
print_list(P)

pos = [[5,3], [1,3], [2,5]] # 구하고자 하는 최단경로의 [시작, 끝] 좌표
for start, end in pos: # 경로 출력
    print(f'The shortest path({start}, {end}) is V{start}', end=' → ')
    path(P, start, end)
    print(f'V{end}')