import sys
sys.stdin = open("같은모양찾기.txt")

N = int(input())  # 10
arr = [list(map(int, input())) for _ in range(N)]

P = int(input())  # 3
pattern = [list(map(int, input())) for _ in range(P)]
# print(pattern[2][::-1])

new_180 = []
for c in range(P-1, -1, -1):
    new_180.append(pattern[c][::-1])
# print(new_180)


# 원래 패턴
def check_00(x, y):
    global P, arr
    for a in range(P):
        for b in range(P):
            if arr[x+a][y+b] != pattern[a][b]:
                return 0    # 패턴 다름
    return 1    # 패턴 같음

# 90도 회전
def check_90(x, y):
    global P, arr
    for a in range(P):
        for b in range(P):
            if arr[x+a][y+b] != pattern[b][a]:
                return 0
    return 1

# 180도 회전
def check_180(x, y):
    global P, arr, new_180
    for a in range(P):
        for b in range(P):
            if arr[x+a][y+b] != new_180[a][b]:
                return 0
    return 1

# 270도 회전
def check_270(x, y):
    global P, arr
    for a in range(P):
        for b in range(P):
            if arr[x+a][y+b] != pattern[a][b]:
                return 0
    return 1

ans = 0
for i in range(N-P+1):
    for j in range(N-P+1):
        if arr[i][j] == pattern[0][0]:
            ans += check_00(i, j)
            ans += check_90(i, j)
        if arr[i][j] == new_180[0][0]:
            ans += check_180(i, j)
        if arr[j][i] == pattern[0][0]:
            ans += check_270(j, i)
print(ans)