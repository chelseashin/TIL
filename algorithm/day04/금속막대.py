import sys
sys.stdin= open("금속막대.txt")

T = int(input())
for tc in range(T):      # testcase
    N = int(input())
    data = list(map(int, input().split()))
    # data = input()
    # print(data)
    # print(len(data))

    for idx, x in enumerate(data):
        if idx % 2 == 0 and data[idx] in x:

            print(data)


    # su = []
    # for i in range(len(data)):
    #     if i % 2 == 0:
    #         su.append(data[i])
    # print(su)

    # for i in range(N):
    #     for j in range(N):
    #         if i % 2 == 0 and j % 2 == 1:
    #             if data[i] == data[j]:
    #                 print(min(data[i]))


    # print(f"{tc + 1} {}")