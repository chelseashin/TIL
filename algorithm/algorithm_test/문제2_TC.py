import sys
sys.stdin = open("문제2.txt")

T = int(input())     # tc의 수 : 8
for tc in range(T):
    N = int(input())     # 지도의 크기 : N
    # sea = [list(map(int, input().split())) for _ in range(N)]
    sea = [[0 for i in range(N+2)] for i in range(N+2)]
    for i in range(1, N+1):
        sea[i] = [0] + list(map(int, input().split())) + [0]

    # dx = [1, -1, 0, 0]
    # dy = [0, 0, 1, -1]

    # 섬인지 아닌지 판단하여 섬의 개수를 구하는 것
    # def isisland(x, y):
    #     global sea, N
    #     count = 0
    #     max_right = 0
    #     for i in range(x, N+1):
    #         for j in range(y, N+1):
    #             if sea[i][j] == 0:
    #                 right = j-1
    #                 if right > max_right:
    #                     max_right = right
    #                     for s in range(4):
    #                         if sea[i+dx[i]][j-1+dy[i]] != 0:
    #     return count
    #
    # # 섬들의 개수
    # island = 0
    # for i in range(1, N+1):
    #     for j in range(1, N+1):
    #         if sea[i][j] >= 0:
    #             sea[i][j] == 99    # 땅이 있으면 모두 99로 바꿔줌
    #             if sea[i][j] == 99:
    #                 island += isisland(i, j)
    # print(island)



    # 가장 높은 섬의 높이
    max_height = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if sea[i][j] > max_height:
                max_height = sea[i][j]
    # print(max_height)

    # island : 섬들의 개수, max_height : 가장 높은 섬의 높이
    print("#{} {} {}".format(tc+1, "island", max_height))