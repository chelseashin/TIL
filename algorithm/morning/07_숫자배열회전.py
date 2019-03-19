import sys
sys.stdin = open("숫자배열회전.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    cube90 = []
    for i in range(N):
        turn90 = []
        for j in range(N):
            turn90.append(arr[N - j - 1][i])
        cube90.append(turn90)
    # print(cube90)

    cube180 = []
    for i in range(N):
        turn180 = []
        for j in range(N):
            turn180.append(arr[N-i-1][N-j-1])
        cube180.append(turn180)
    # print(cube180)

    cube270 = []
    for i in range(N):
        turn270 = []
        for j in range(N):
            turn270.append(arr[j][N-i-1])
        cube270.append(turn270)
    # print(cube270)

    # result = cube90 + cube180 + cube270
    # result = []
    # for a in range(N):
    #     result.append(cube90[a])
    #     result.append(cube180[a])
    #     result.append(cube270[a])
    z = zip(cube90, cube180, cube270)
    # print(list(z))

    print("#{}".format(tc + 1))
    for row in z:
        for a in row:
            print(*a, sep="", end=" ")
        print()


