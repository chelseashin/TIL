import sys
sys.stdin = open("도약.txt")

N = int(input())
# leaf = []
# for i in range(N):
#     leaf.append(int(input()))
leaf = [int(input()) for _ in range(N)]
leaf.sort()    # 오름차순으로 정렬

# 3중루프로 풀어야 함!
jump = 0   # 전체 점프 경우의 수
for i in range(N-2):    # 시작 위치
    for j in range(i+1, N-1):    # 첫번째 점프
        jump1 = leaf[j] - leaf[i]
        for k in range(j+1, N):    # 두번째 점프
            jump2 = leaf[k] - leaf[j]
            if jump1 <= jump2 <= jump1 * 2:
                jump += 1
            if jump2 > jump1*2:   # 이전에 뛴 거리보다 두배 이상이면 탈출
                break
print(jump)
