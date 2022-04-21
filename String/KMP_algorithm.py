def InitNext(p:str): # Next list 생성
    global next
    M = len(p)
    i, j = 0, -1 # i, j 초기화
    while i < M:
        next[i] = next[j] if p[i] == p[j] else j # 개선된 코드(p[i]와 p[j]가 동일하면 next[j]를 넣음)
        while j >= 0 and p[i] != p[j]: # 불일치가 일어났을 때
            j = next[j]
        i += 1
        j += 1

def KMP(p:str, t:str): # p: 찾으려는 값, t: text
    M, N = len(p), len(t)
    InitNext(p)
    i, j = 0, 0
    while i < N: # t의 끝까지 도달할 때까지 반복
        if j == M:
            print(f'패턴이 발생한 위치: {i-M}') # pattern 위치 출력
            j = 0 # 아직 t의 끝에 도달하지 않았으므로 pattern을 추가적으로 탐색
        while j >= 0 and t[i] != p[j]:
            j = next[j]
        i += 1
        j += 1
    if j == M:
        print(f'패턴이 발생한 위치: {i-M}') # pattern 위치 출력
    print("탐색 종료")

if __name__ == '__main__':
    text = input() # text 입력
    pattern = input() # 찾으려는 pattern 입력

    next = [-1] * len(pattern) # pattern 크기와 동일한 next 배열 선언
    KMP(pattern, text) # 입력된 text에서 pattern의 위치 탐색