import decimal
import numpy as np

def print_list(li, s, t): # dp, cal list를 출력하는 함수
    for row in range(t+1): 
        for col in range(s+1):
            print(li[row][col], end=' ')
        print()

def EditDistance(source, target):
    ins_cost =decimal.Decimal('0.7')  # 삽입 비용
    del_cost = decimal.Decimal('0.5') # 삭제 비용

    s = len(source) # source 길이
    t = len(target) # target 길이
    dp = [[0] * (t+1) for _ in range(s + 1)] # dp list 생성
    cal = [[0] * (t+1) for _ in range(s + 1)] # 각 지점에서 연산 방법을 저장할 cal list 생성(교환: 1, 삽입: 2, 삭제: 3)

    for i in range(1, s+1): # 0열 초기화
        dp[i][0] = dp[i-1][0] + del_cost
        cal[i][0] = 3
    for j in range(1, t+1): # 0행 초기화
        dp[0][j] = dp[0][j-1] + ins_cost
        cal[0][j] = 2

    for i in range(1, s+1):
        for j in range(1, t+1):
            change_cost = 0 if source[i-1] == target[j-1] else decimal.Decimal('0.3') # 교환 비용이 0인지 아닌지 판별
            dp[i][j] = min(dp[i-1][j-1]+change_cost, dp[i-1][j]+del_cost, dp[i][j-1]+ins_cost) # 교환, 삽입, 삭제에 따른 최소 비용 계산
            if  dp[i][j] == dp[i-1][j-1]+change_cost: # 교환에서 최소가 발생한 경우
                if change_cost == 0: # 교환 비용이 0이면
                    cal[i][j] = 0 # 비용이 들지 않음
                else: # 교환 비용이 0이 아니면
                    cal[i][j] = 1 # 교환 비용 발생
            elif dp[i][j] == dp[i-1][j]+del_cost: # 삭제에서 최소가 발생한 경우
                cal[i][j] = 3 # 삭제 발생
            else: # 삽입에서 최소가 발생한 경우
                cal[i][j] = 2 # 삽입 발생

    dp = np.array(dp).T # Transpose
    cal = np.array(cal).T # Transpose

    print_list(dp, s, t) # dp list 출력

    # dp[-1][-1]로 오기까지의 연산 방식을 거꾸로 순회하며 찾음
    # cal에 저장된 값이 0인 경우 교환 비용이 0인 경우이므로 row, col을 한 칸씩 줄임
    # cal에 저장된 값이 1인 경우 교환 비용이 발생한 경우이므로 row, col을 한 칸씩 줄임
    # cal에 저장된 값이 2인 경우 삽입 비용이 발생한 경우이므로 row를 한 칸 줄임
    # cal에 저장된 값이 3인 경우 삭제 비용이 발생한 경우이므로 col을 한 칸 줄임
    col = s # dp[-1][-1] 위치의 col 저장
    row = t # dp[-1][-1] 위치의 row 저장
    method = list()
    while row >= 0 and col >= 0: # 연산 순서 구하기
        if cal[row][col] == 0: # 교환 발생(비용 0)
            row -= 1
            col -= 1
        elif cal[row][col] == 1: # 교환 발생
            row -= 1
            col -= 1
            method.append(1) # 교환을 의미하는 1 저장
        elif cal[row][col] == 2: # 삽입 발생
            row -= 1
            method.append(2) # 삽입을 의미하는 2 저장
        elif cal[row][col] == 3:  # 삭제 발생
            col -= 1
            method.append(3) # 삭제를 의미하는 3 저장

    method.reverse()
    # dp[-1][-1]에서부터 거꾸로 연산 방식을 찾아갔으므로 다시 반대로 출력하기 위해 reverse
    for m in method: # 저장된 값이 1이면 교환, 2면 삽입, 3이면 삭제
        if m == 1:
            print(f'교환 연산: {0.3}', end='  ')
        elif m == 2:
            print(f'삽입 연산: {ins_cost}', end='  ')
        elif m == 3:
            print(f'삭제 연산: {del_cost}', end='  ')
    print()
    print(f'Levenshtein Distance = {dp[-1][-1]}') # 최소 비용 출력

source = ['GUMBO', 'Levenshtein', 'TACTG', '데이타마이닝']
target = ['GAMBOL', 'Meilenstein', 'CATGACTG', '데이터베이스설계']

for i in range(4):
    EditDistance(source[i], target[i])
    print()