import sys
sys.stdin = open("Ladder1.txt")

T = 10
Size = 100
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(Size)]
    # print(data)
    # print(len(data))  => 100

    result = 0
    for i in range(len(data)):
        for j in range(len(data)):
            while i-1 < 100 and j-1 < 100:
                if data[i][j] == 2:
                    data[i][j+1] += 1
                    if data[i+1][j] == 1:
                        data[i+1][j] += 1
                    elif data[i-1][j] == 1:
                        data[i-1][j] += 1

    if data[0][j] == 2:
        print(f"#{tc+1} {result}")