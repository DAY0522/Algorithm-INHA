# 숫자판 배열 선언
arr = [[3, 4, 9, -2, 2, 51, -23, 2, -1],
[223, 7, 8, -11, 5, -99, 2, 3, -4],
[2, 51, -23, -23, 6, 3, 2, 4, 5],
[5, -99, 2, -1, 32, 2, 5, -99, 2],
[6, 3, 3, -4, 2, -1, 6, 3, 3],
[32, 2, 4, 5, 3, -4, 2, -1, 4],
[4, 4, 23, 6, 2, -1, 3, -4, 34],
[78, 32, 1, 7, 3, -4, -23, -23, 6]]

dp = [list(arr[0])] # 최댓값을 저장할 dp 배열 선언, 첫 번째 줄은 이미 정해진 것이므로 그대로 할당
route = list() # 경로의 방향을 저장할 배열
len_row = len(arr) # 숫자판 배열의 행
len_col = len(arr[0]) # 숫자판 배열의 열

for row in range(1, len_row):
    dp_row = list()  # 각 열에 대한 최댓값을 저장할 dp 배열
    dp_route = list() # 경로를 저장할 배열
    for col in range(0, len_col):
        if col == 0: # col이 맨 왼쪽이면 왼쪽 대각선에서 내려오는 경우가 없으므로 예외처리
            max_val = max(dp[row - 1][col], dp[row - 1][col + 1])
            dir = "straight" if max_val == dp[row - 1][col] else "right" # 어느 방향에서 온 건지 저장
        elif col == (len_col-1): # col이 맨 오른쪽이면 오른쪽 대각선에서 내려오는 경우가 없으므로 예외처리
            max_val = max(dp[row - 1][col - 1], dp[row - 1][col])
            dir = "straight" if max_val == dp[row - 1][col] else "left" # 어느 방향에서 온 건지 저장
        else:
            max_val = max(dp[row-1][col-1], dp[row-1][col], dp[row-1][col+1])
            if max_val == dp[row - 1][col]: # 어느 방향에서 온 건지 저장
                dir = "straight"
            elif max_val == dp[row - 1][col-1]:
                dir = "left"
            else:
                dir = "right"
        dp_row.append(max_val + arr[row][col]) # 이전 경로까지의 최댓값과 현재 값을 더함
        dp_route.append(dir)
    dp.append(dp_row)
    route.append(dp_route)

max_i = dp[-1].index(max(dp[-1]))
cur_row = len_row - 1
cur_col = max_i

# route를 찾는 부분
route_val = [arr[cur_row][cur_col]] # 지나온 값들을 저장할 배열
while(cur_row > 0):
    cur_dir = route[cur_row - 1][cur_col] # 현재 인덱스를 오기 전의 방향 저장
    cur_row -= 1
    if cur_dir == "straight": # 바로 위에서 내려온 경우
        # row는 1 줄고, col은 그대로
        route_val.append(arr[cur_row][cur_col])
    elif cur_dir == "right": # 오른쪽에서 내려온 경우
        # row는 1 줄고, col은 1 증가
        cur_col += 1
        route_val.append(arr[cur_row][cur_col])
    else: # 왼쪽에서 내려온 경우
        # row는 1 줄고, col은 1 감소
        cur_col -= 1
        route_val.append(arr[cur_row][cur_col])

print(f'최댓값: {max(dp[-1])}')
# 경로 출력
for i in range(len_row-1, 0, -1):
    print(route_val[i], end=' → ')
print(route_val[0])