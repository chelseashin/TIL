import sys
sys.stdin = open("05.txt")

def check_babyGin(c):
    global flag
    check = 0

    if c % 2 == 0:
        if p1[0] == p1[1] and p1[1] == p1[2]: check += 1
        if p1[0] + 1 == p1[1] and p1[1] + 1 == p1[2]: check += 1

    elif c % 2 != 0:
        if p2[0] == p2[1] and p2[1] == p2[2]: check += 1
        if p2[0] + 1 == p2[1] and p2[1] + 1 == p2[2]: check += 1

    if check != 0:
        flag = 1
        return

def perm(n, k, c):
    if c % 2 == 0:
        if k == n:
            check_babyGin(c)
        else:
            for i in range(k, n):
                p1[k], p1[i] = p1[i], p1[k]
                perm(n, k + 1, c)
                p1[k], p1[i] = p1[i], p1[k]
    elif c % 2 != 0:
        if k == n:
            check_babyGin(c)
        else:
            for i in range(k, n):
                p2[k], p2[i] = p2[i], p2[k]
                perm(n, k + 1, c)
                p2[k], p2[i] = p2[i], p2[k]

T = int(input())
for tc in range(T):
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    ans = 0
    for i in range(len(cards)):
        if i % 2 == 0:
            p1.append(cards[i])
            if len(p1) >= 3:
                flag = 0
                perm(len(p1), 0, i)
                if flag:
                    ans = 1
                    break
        else:
            p2.append(cards[i])
            if len(p2) >= 3:
                flag = 0
                perm(len(p2), 0, i)
                if flag == 1:
                    ans = 2
                    break

    print("#{} {}".format(tc+1, ans))

