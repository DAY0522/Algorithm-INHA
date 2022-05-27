def knapsack(weight, j):
    n = len(j)
    dp = [[0 for _ in range(weight+1)] for _ in range(n+1)] # dp를 위한 2차원 리스트 초기화
    for i in range(1, n+1):
        for w in range(1, weight+1): # 각 칸을 순회
            # 점화식에 따라 계산
            if j[i-1][0] <= w: # i번째를 담을 수 있는 경우
                dp[i][w] = max(dp[i-1][w], j[i-1][1]+dp[i-1][w-j[i-1][0]])
            else: # i번째를 담을 수 없는 경우
                dp[i][w] = dp[i-1][w]
    return dp[n][weight]

if __name__ == '__main__':
    weight = 15 # 배낭 무게
    jewelry = [[5,5],[10,7],[7,10],[3,6],[4,8],[11,20]]

    weight2 = 30 # 배낭 무게
    jewelry2 = [[3,5],[7,7],[8,10],[5,6],[6,8],[13,20],[11,18],[2,5]]

    print(f'입력에 대하여 가방에 담은 보석의 최대 가치: {knapsack(weight, jewelry)}')
    print(f'입력에 대하여 가방에 담은 보석의 최대 가치: {knapsack(weight2, jewelry2)}')