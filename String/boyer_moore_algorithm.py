from collections import defaultdict

def InitSkip(p): # skip 배열 생성
    M = len(p) # 패턴 크기
    for i in range(M):
        skip[p[i]] = M-i-1 # 뒤에서 몇 번째에 위치하는지 저장

def MisChar(p, t):
    M = len(p) # 패턴 크기
    N = len(t) # 텍스트 크기
    pos = list() # 위치 저장할 배열 생성
    InitSkip(p) # skip 배열 생성

    i = M-1
    j = M-1
    while i < N: # i가 N보다 작을 때까지 탐색
        while t[i] != p[j]: # 불일치
            k = skip[t[i]]
            i = i+M-j if M-j > k else i+k
            if i >= N: # i가 N보다 크면 종료
                return pos # 패턴 위치
            j = M - 1
        i -= 1
        j -= 1
        if (j < 0): # 참이면 패턴을 찾은 것이므로 pos에 패턴 위치 저장
            pos.append(i+1) # 위치 저장
            i = i + M + 1
            j = M - 1
    return pos # 패턴 위치


if __name__ == '__main__':
    # 파일 불러오기
    with open('RFC2616_modified.txt', 'r') as file:  # 파일을 읽기 모드로 열람
        t = file.read()  # 파일의 내용을 변수에 저장

    # Pattern 문자
    p = "similar"
    skip = defaultdict(lambda: len(p))  # 기본값을 pattern의 길이로 지정(dict에 저장되지 않은 값은 모두 p의 길이를 가짐)

    pos = MisChar(p, t) # 불필요한 탐색 스킵

    # 찾은 pattern의 정보 출력
    print(f'찾은 pattern(\'{p}\')의 개수: {len(pos)}')
    for po in pos:
        print(f'position: {po}')
        '''
        for i in range(len(p)):
            print(t[po + i], end='')
        print()
        '''