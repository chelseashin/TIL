import sys
sys.stdin = open("Ladder1.txt")

T = 10
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    # print(data)
    # print(len(data))  => 100
    floor = len(data) - 1    # => 99
    ice = data[floor].index(2)   # 마지막 줄에서 2가 있는 위치 반환
    # print(ice)

    while floor:
        if ice != 0 and ice != 99:
            if data[floor][ice-1] == 0 and data[floor][ice+1] == 0:
                floor -= 1
            if data[floor][ice-1] == 1 and data[floor][ice+1] == 0:
                data[floor][ice] = 0
                ice -= 1
            if data[floor][ice-1] == 0 and data[floor][ice+1] == 1:
                data[floor][ice] = 0
                ice += 1

        if ice == 0 and data[floor][ice+1] == 0:
            floor -= 1

        if ice == 0 and data[floor][ice+1] == 1:
            data[floor][ice] = 0
            ice += 1

        if ice == 99 and data[floor][ice-1] == 0:
            floor -= 1

        if ice == 99 and data[floor][ice-1] == 1:
            data[floor][ice] = 0
            ice -= 1

    result = ice
    print(f"#{tc+1} {result}")






    # for i in range(len(data)):
    #     for j in range(len(data)):
    #         while i-1 < 100 and j-1 < 100:
    #             if data[i][j] == 2:
    #                 data[i][j+1] += 1
    #                 if data[i+1][j] == 1:
    #                     data[i+1][j] += 1
    #                 elif data[i-1][j] == 1:
    #                     data[i-1][j] += 1
    #
    # if data[0][j] == 2:
