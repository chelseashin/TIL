import sys
sys.stdin = open("문제2.txt")

T = int(input())     # tc의 수 : 8
for tc in range(T):
    N = int(input())     # 지도의 크기 : N
    # sea = [list(map(int, input().split())) for _ in range(N)]
    sea = [[0 for i in range(N+2)] for i in range(N+2)]
    for i in range(1, N+1):
        sea[i] = [0] + list(map(int, input().split())) + [0]

    # 가장 높은 섬의 높이
    max_height = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if sea[i][j] > max_height:
                max_height = sea[i][j]
    # print(max_height)

    # island : 섬들의 개수, max_height : 가장 높은 섬의 높이
    print("#{} {} {}".format(tc+1, "island", max_height))