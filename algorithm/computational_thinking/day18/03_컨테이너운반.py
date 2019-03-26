import sys
sys.stdin = open("03.txt", "r")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    weights = sorted(w)
    tons = sorted(t)

    ans = 0
    while True:
        if len(tons) == 0 or len(weights) == 0:
            break
        if tons[-1] >= weights[-1]:
            ans += weights[-1]
            weights.pop()
            tons.pop()
        elif tons[-1] < weights[-1]:
            weights.pop()
    print("#{} {}".format(tc+1, ans))

# 다른 풀이
#     w.sort(), t.sort()
#     sum = 0
#     while len(w) > 0 and len(t) > 0:
#         if w[-1] <= t[-1]:
#             sum += w[-1]
#             w.pop(), t.pop()
#             continue
#         elif w[-1] > t[-1]:
#             w.pop()
#             continue
#     print("#{} {}".format(tc+1, sum))