import sys
sys.stdin = open("소수.txt")

def issosu(a, b):
    result = []
    for i in range(a, b+1):
        if i == 2:
            result.append(i)
        elif i > 2:
            for j in range(2, int(i**0.5)+1):
                if not i%j:
                    break
            else:
                result.append(i)
    return result

T = 3
for i in range(T):
    a, b = map(int, input().split())    # 2, 10
    m, n = min(a, b), max(a, b)

    L = sorted(issosu(m, n))

    t = len(L)
    k = L[0] + L[-1]

    print(t)
    print(k)


    # sosu = [0]*100
    #
    # smin = 987654321
    # smax = 0
    # for i in range(a, b+1):
    #     if i*i > 100: break
    #     if sosu[i]:
    #         continue
    #     for j in range(i*2, 101, i):
    #         sosu[j] = 1