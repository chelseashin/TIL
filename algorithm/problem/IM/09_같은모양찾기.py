import sys
sys.stdin = open("같은모양찾기.txt")

N = int(input())  # 10
arr = [list(map(int, input())) for _ in range(N)]

P = int(input())  # 3
pattern = [list(map(int, input())) for _ in range(P)]

# 나의풀이
def check_pattern(x, y):
    global P
    for a in range(P):
        for b in range(P):
            # 좌표 대 좌표로만 비교하면 훨씬 효율적임!
            # 하나하나 다 체크하기보다 하나라도 아니면 바로 0을 리턴
            if arr[x+a][y+b] != pattern[a][b]:
                return 0    # 패턴 다름
    return 1    # 패턴 같음

ans = 0
for i in range(N-P+1):
    for j in range(N-P+1):
        if arr[i][j] == pattern[0][0]:
            ans += check_pattern(i, j)

print(ans)


# 다른 풀이
# total = 0
# case = []
#
# for i in range(N-P+1):
#     for j in range(N-P+1):
#         for x in range(P):
#             case.append(arr[i+x][j:j+P])
#         if case == pattern:
#             total += 1
#         case = []
#
# print(total)

# 좋은 풀이

sol = 0
for i in range(N-P+1):           # 모눈종이 시작행 제어
    for j in range(N-P+1):       # 모눈종이 시작열 제어
        flag = 0
        for k in range(P):       # 패턴행
            for l in range(P):   # 패턴열
                if arr[i+k][j+l] != pattern[k][l]:  # 좌표 다르면 flag = 1
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 0:   # 좌표 다른 조건에 걸리지 않으면 패턴 찾음 : 0 이면
            sol += 1    # 합계 += 1
print(sol)