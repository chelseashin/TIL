import sys
sys.stdin = open("05.txt")

def check_babyGin1(arr):
    global flag
    check = 0
    if arr[0] == arr[1] and arr[1] == arr[2]: check += 1

    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]: check += 1

    if check == 1:
        flag = 1
        return

def check_babyGin2(arr):
    global flag
    check = 0
    if arr[0] == arr[1] and arr[1] == arr[2]: check += 1

    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]: check += 1

    if check == 1:
        flag = 1
        return

def perm(n, k):
    global arr
    if k == n:
        check_babyGin(arr)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]

T = int(input())
for tc in range(T):
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    flag = 0
    ans = 0
    for i in range(len(cards)):
        if i % 2 == 0:
            p1.append(cards[i])
            if len(p1) >= 3:
                perm(len(p1), 0, i)
                if flag == 1:    # and ans == 0:
                    ans = 1
        else:
            p2.append(cards[i])
            if len(p2) >= 3:
                perm(len(p2), 0, i)
                if flag == 1:    # ans == 0:
                    ans = 2

    print("#{} {}".format(tc+1, ans))

