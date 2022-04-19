import random
import time

def Odd_Even(arr):
    isSorted = False
    N = len(arr)-1
    while not isSorted:
        isSorted = True
        for i in range(0, N, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = False
        #print("odd index")
        #for a in arr:
        #    print(a, end=' ')
        #print()

        for i in range(1, N, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = False
        #print("even index")
        #for a in arr:
        #    print(a, end=' ')
        #print()
    return


def CheckSort(a:list): # 정렬 결과 체크 함수
    for i in range(len(a)-1):
        if a[i]>a[i+1]: # 앞에 있는 수가 더 크면 정렬이 잘못된 것임
            print("정렬 오류!!")
            exit()
    print("정렬 완료")

"""
# 세 개의 정수 베열 정렬
nums = [ 4, 13, 2, 5, 6, 70, 8, 3, 10, 11, 24, 23, 21, 7, 9, 12]
Odd_Even(nums)
print("\n최종 정렬 결과")
for n in nums:
    print(n, end=' ')
print()
CheckSort(nums)
"""

# 임의의 정수 배열 정렬
sizes = [1000, 5000, 10000] # 입력의 크기를 미리 list로 만들어 놓음
for s in sizes:
    nums = [random.randrange(0, 1001) for _ in range(s)] # 정렬할 list 생성

    start = time.time() # 시작 시간
    Odd_Even(nums)
    end = time.time() # 끝 시간
    print(f"입력의 크기: {s}")
    CheckSort(nums) # 정렬이 잘 됐는지 확인
    print(f"Odd Even Sort 실행 시간: {end-start:.5f}sec") # 총 걸린 시간 출력
    print()
