# 이진탐색
import sys
sys.stdin = open("이진탐색.txt")

def binarySearch(P, K):
    start = 1
    end = P
    cnt = 0
    while start <= end:
        cnt += 1
        middle = start + (end - start) // 2

        if K == middle:  # 검색 성공
            return cnt
        elif K <= middle:
            end = middle
        else:
            start = middle

T = int(input())
for tc in range(T):
    P, Pa, Pb = map(int, input().split())

    cnt_a = binarySearch(P, Pa)
    cnt_b = binarySearch(P, Pb)

    if cnt_a > cnt_b:
        ans = "B"
    elif cnt_a < cnt_b:
        ans = "A"
    else:
        ans = 0

    print(f"#{tc + 1} {ans}")
