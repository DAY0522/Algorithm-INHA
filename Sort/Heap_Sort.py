import random
import time

def minHeapSort(a:list):
    n = len(a)-1  # heap 크기
    for i in range(n//2, 0, -1): # 배열 a를 heap으로 변환
        heapify_dec(a, i, n)
    print()
    for i in range(n-1, 0, -1):
        a[1], a[i+1] = a[i+1], a[1]
        heapify_dec(a, 1, i)

def heapify_dec(a:list, h, m):
    # 큰수를 위로
    v = a[h] # 부모 노드
    j = 2*h # h의 왼쪽 자식
    while(j <= m):
        if j < m and a[j] < a[j+1]: # 왼쪽 자식과 오른쪽 자식 비교
            j = j+1
        if v >= a[j]: # 부모가 해당 자식보다 크면 멈춤
            break
        else: # 부모가 자식보다 작으면
            a[j//2] = a[j] # 부모가 자식보다 작을 경우 부모와 값을 바꿈
        j *= 2
    a[j//2] = v;

def MaxHeapSort(a:list):
    n = len(a)-1  # heap 크기
    for i in range(n//2, 0, -1): # 배열 a를 heap으로 변환
        heapify_inc(a, i, n)

    for i in range(n-1, 0, -1):
        a[1], a[i+1] = a[i+1], a[1]
        heapify_inc(a, 1, i)

def heapify_inc(a:list, h, m):
    # 작은 수를 위로
    v = a[h]
    j = 2*h
    while(j <= m):
        if j < m and a[j] > a[j+1]:
            j = j+1
        if v <= a[j]:
            break
        else:
            a[j//2] = a[j]
        j *= 2
    a[j//2] = v;

def CheckSort_inc(a:list): # 오름차순 정렬 결과 체크 함수
    for i in range(1, len(a)-1):
        if a[i]>a[i+1]: # 앞에 있는 수가 더 크면 정렬이 잘못된 것임
            print("정렬 오류!!")
            exit()
    print("정렬 완료")

def CheckSort_dec(a:list): # 내림차순 정렬 결과 체크 함수
    for i in range(1, len(a)-1):
        if a[i]<a[i+1]: # 앞에 있는 수가 더 크면 정렬이 잘못된 것임
            print("정렬 오류!!")
            exit()
    print("정렬 완료")

nums = [0, 6, 2, 8, 1, 3, 9, 4, 5, 10, 7]
MaxHeapSort(nums)
print("MaxHeap 정렬 결과")
for i in range(1,len(nums)):
    print(nums[i], end=' ')
print()

nums = [0, 6, 2, 8, 1, 3, 9, 4, 5, 10, 7]
minHeapSort(nums)
print("minHeap 정렬 결과")
for i in range(1,len(nums)):
    print(nums[i], end=' ')
print()


sizes = [10000, 50000, 100000, 500000, 1000000] # 입력의 크기를 미리 list로 만들어 놓음
for s in sizes:
    nums = [random.randrange(1, 1000) for _ in range(s)] # 정렬할 list 생성

    start = time.time() # 시작 시간
    MaxHeapSort(nums)
    end = time.time() # 끝 시간
    print("Maxheap sorting complete!")
    print(f"Maxheap sorting (N={s}) time cost: {end-start:.5f}sec") # 총 걸린 시간 출력
    CheckSort_dec(nums) # 정렬이 잘 됐는지 확인

    nums = [random.randrange(1, 1000) for _ in range(s)] # 정렬할 list 생성

    start = time.time() # 시작 시간
    minHeapSort(nums)
    end = time.time() # 끝 시간
    print("minheap sorting complete!")
    print(f"minheap sorting (N={s}) time cost: {end-start:.5f}sec") # 총 걸린 시간 출력
    CheckSort_inc(nums) # 정렬이 잘 됐는지 확인

    print() # 출력 결과 가독성을 위한 줄바꿈
