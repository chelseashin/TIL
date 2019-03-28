import sys
sys.stdin = open("색종이(초).txt")

N = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]

for i in range(N):
    L, R = map(int, input().split())
    # 방법 1 - 색종이 붙이기
    for i in range(L, L+10):
        for j in range(R, R+10):
            arr[i][j] = 1

# 도화지에서 면적 구하기
sum = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] != 0:
            sum += 1
print(sum)

    # 방법 2
    # 첫 값을 받아서 이를 함수로 돌려서 종이를 붙임
    # for i in range(10):
    #     for j in range(10):
    #         arr[S+i][G+i] = 1