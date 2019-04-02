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

    print("#{} {}".format(tc+1, result))


# 다른 풀이

# for n in range(1, T + 1):
#     N = int(input())
#     L = []
#     for i in range(100):
#         no = list(map(int, input().split()))
#         L += [no]
#
#     for i in range(100):
#         if L[99][i] == 2:
#             start = i
#             break
#     up = 98
#     while up != 0:
#         if start < 99 and L[up][start + 1] == 1:
#             while start != 99:
#                 start += 1
#                 if L[up][start] == 0:
#                     start += -1
#                     break
#         elif start > 0 and L[up][start - 1] == 1:
#             while start != 0:
#                 start += -1
#                 if L[up][start] == 0:
#                     start += 1
#                     break
#
#         up += -1
#
#     print(f"#{n} {start}")


# 다른 풀이

# deg = [-1, 1]
# for test_case in range(10):
#     tc = int(input())
#     ladder = []
#     for i in range(100):
#         ladder.append(list(map(int, input().split())))
#     cnt = 0
#     col = 0
#     for i in ladder[-1]:
#         if i == 2:
#             col = cnt
#             break
#         cnt += 1
#
#     for row in range(1, 101):
#         check = 0
#         for plus_col in deg:
#             # print(col + plus_col, ladder[-row][col + plus_col])
#             if col + plus_col >= 0 and col + plus_col < 100 and ladder[-row][col + plus_col]:
#                 check = plus_col
#                 col += check
#                 break
#         # print(row, check)
#         if check:
#             while True:
#                 if col < 0 or col >= 100 or not ladder[-row][col]:
#                     break
#                 col += check
#             col -= check
#     print("#{} {}".format(tc, col))



