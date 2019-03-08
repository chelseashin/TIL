import sys
sys.stdin = open("나는학급회장이다.txt")

N = int(input())   # 6
# score = [list(map(int, input().split())) for _ in range(N)]

arr = [[0]*5 for _ in range(4)] # 행을 후보자로, 열을 1, 2, 3 점수대로 4열은 합계
for i in range(N):
    score = list(map(int, input().split()))
    for j in range(1, 4):     # 후보자 3명
        arr[j][score[j-1]] += 1    # 후보자별 점수별 카운트

# 후보자별 합계
for i in range(1, 4):
    for j in range(1, 4):
        arr[i][4] += arr[i][j] * j

# for i in range(1, 4):
#     for j in range(1, 5):
#         print(arr[i][j], end = " ")
#     print()

print(arr)

maxi = 1    # 최고 점수의 인덱스. imax : 1번 후보를 max로 시작
flag = 0
for i in range(2, 4):
    if maxi[4] < arr[i][4]:    # 더 큰 합계를 비교
        maxi = i
    elif arr[maxi][4] == arr[i][4]:    # 동일 합계라면 3점대부터 비교:
        for j in range(3, 1, -1):
            # 두 후보간 더 큰 점수의 후보 탐색
            if arr[maxi][j] == arr[i][j]:
                continue
print(maxi, arr[maxi][4])