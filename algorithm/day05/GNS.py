import sys
sys.stdin = open("GNS_input.txt")

T = int(input())
order = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(T):
    temp = input()    # dummy
    data = list(map(str, input().split()))
    # print(data)

    count = [0] * (len(order))
    for i in range(len(order)):
        for j in range(len(data)):
            if order[i] == data[j]:
                count[i] += 1
    # print(count)

    ans = []
    for i in range(10):
        ans += [order[i]] * count[i]

    print("#{}".format(tc+1))
    print(' '.join(ans))
