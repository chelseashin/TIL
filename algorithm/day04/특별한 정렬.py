# 특별한 정렬
import sys
sys.stdin = open("특별한 정렬.txt")

T = int(input())
for tc in range(T):      # testcase
    N = int(input())
    data = list(map(int, input().split()))
    # print(data)
    up = sorted(data)
    down = sorted(data, reverse = True)
    # print(up)
    # print(down)

    special = []
    for i in range(int(len(data)/2)):
        special.append(down[i])
        special.append(up[i])
    # print(special[:10])

    print(f"#{tc + 1}", end =" ")
    for i in range(10):
        print(special[i], end = " ")
    print()