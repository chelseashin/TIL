import sys
sys.stdin = open("배부른 돼지.txt")

n = int(input())
data = [list(map(str, input().split())) for i in range(n)]
# print(data)

# 예외처리
if n == 0:
    print("F")
else:
    Max = 0
    Min = 987654321
    for i in range(n):
        if data[i][1] == "Y":
            if Min > int(data[i][0]):
                Min = int(data[i][0])

        elif data[i][1] == "N":
            if Max < int(data[i][0]):
                Max = int(data[i][0])

    if Max < Min:
        print(Min)
    else:
        print("F")

