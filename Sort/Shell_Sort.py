import random
import time

def ShellSort(a:list): # ShellSort 함수
    h = 1
    while h < len(a): # 첫 번째 h값 계산
        h = 3*h + 1 # 증가식
    while h > 0: # h값을 감소시키며 진행
        for i in range(h, len(a)): # sub list sort
            v = a[i]
            while i >= h and a[i-h] > v: # 앞에 있는 값이 수가 더 크면 교환
                a[i] = a[i-h]
                i -= h
            a[i] = v
        h //= 3 # 감소식

def CheckSort(a:list): # 정렬 결과 체크 함수
    for i in range(len(a)-1):
        if a[i]>a[i+1]: # 앞에 있는 수가 더 크면 정렬이 잘못된 것임
            print("정렬 오류!!")
            exit()
    print("정렬 완료")

sizes = [100000, 500000, 1000000, 5000000, 10000000] # 입력의 크기를 미리 list로 만들어 놓음
for s in sizes:
    print(f"입력의 크기 : {s}\n증가식: 3h+1, 감소식: h/3")
    nums = [random.randrange(1, 1000) for _ in range(s)] # 정렬할 list 생성

    start = time.time() # 시작 시간
    ShellSort(nums)
    end = time.time() # 끝 시간
    print(f"Shell Sort 실행 시간: {end-start:.5f}sec") # 총 걸린 시간 출력
    CheckSort(nums) # 정렬이 잘 됐는지 확인
    print() # 출력 결과 가독성을 위한 줄바꿈