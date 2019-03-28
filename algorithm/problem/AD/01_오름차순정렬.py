import sys
sys.stdin = open("01.txt")

# 정렬함수 사용
# N = int(input())
# num = list(map(int, input().split()))
# print(*sorted(num))


# 정렬 함수 만들기
def sort(s, e):
    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def Qsort(s, e):
    if s >= e: return
    p, t = e, s
    for l in range(s, e):
        if arr[l] < arr[p]:


def Msort(s, e):
    if s>=e: return
    m=(s+e)//2
    Msort(s, m)
    Msort(m+1, e)
    l, r, t = s, m+1, s
    while l <= m and r <= e:
        if arr[l] < arr[r]:     # 왼쪽 영역이 작으면 왼쪽 영역값을 임시버퍼로
            temp[t] = arr[l]
            t += 1
            r += 1

    while l<=m:    # 왼쪽 영역이 아직 남아있으면 나머지를 임시버퍼로
        temp[t] = arr[l]
        t += 1
        r += 1

    while r <= e:
        temp[t] = arr[r]
        t += 1
        r += 1
    for i in range(s, e+1, )


    # main
    N = int(input())
    arr = list(map(int, input().split()))
    temp = [0] * N
    # sort(0, N-1)
    # Qsort(0, N-1)
    Msort(0, N-1)
    for i in range(N):
        print(arr[i], end=" ")