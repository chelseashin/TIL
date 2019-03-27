import sys
sys.stdin = open("사냥꾼.txt")

# 나의 풀이
# 사냥꾼이 토끼를 몇 마리 잡는지 구하는 함수
def catch_rabbit(x, y):
    global jido, N
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    count = 0
    for i in range(8):
        for dis in range(1, N):
            if jido[x + dx[i] * dis][y + dy[i] * dis] == 0:
                continue
            else:
                if jido[x+dx[i]*dis][y+dy[i]*dis] == 1 or jido[x+dx[i]*dis][y+dy[i]*dis] == 3:
                    break
                elif jido[x + dx[i] * dis][y + dy[i] * dis] == 2:
                    jido[x + dx[i] * dis][y + dy[i] * dis] = 9
                    count += 1
    return count

T = int(input())
for tc in range(T):
    N = int(input())
    jido = [[3] * (N+2) for _ in range(N+2)]    # 주위를 돌로 둘러싼 지도 만들기
    for n in range(N):
        jido[n+1] = [3] + list(map(int, input().split())) + [3]

    rabbits = 0
    for i in range(N+2):
        for j in range(N+2):
            if jido[i][j] == 1:
                rabbits += catch_rabbit(i, j)

    print("#{} {}".format(tc+1, rabbits))

# 다른 풀이
# def catch_rabbit(x, y):
#     global jido, N
#     dx = [-1, -1, 0, 1, 1, 1, 0, -1]
#     dy = [0, 1, 1, 1, 0, -1, -1, -1]
#
#     count = 0
#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         while True:
#             if nx < 0 or nx >= N: break
#             if nx < 0 or ny >= N: break
#             if jido[nx][ny] == 1: break
#             if jido[nx][ny] == 3: break
#             if jido[nx][ny] == 0:
#                 nx += dx[i]
#                 ny += dy[i]
#                 continue
#             if jido[nx][ny] == 2:
#                 count += 1
#                 nx += dx[i]
#                 ny += dy[i]
#     return count
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     jido = [list(map(int, input().split())) for _ in range(N)]
#
#     rabbits = 0
#     for i in range(N):
#         for j in range(N):
#             if jido[i][j] == 1:
#                 rabbits += catch_rabbit(i, j)
#
#     print("#{} {}".format(tc+1, rabbits))

# 다른 풀이 2

# def solve():
#     global ans
#     dx = [-1, 1, 0, 0, -1, 1, 1, -1]
#     dy = [0, 0, 1, -1, 1, 1, -1, -1]
#     for i in range(len(hunter)):    # 사냥군 명수만큼
#         for j in range(8):          # 8방향 검색
#             x, y = hunter[i]
#             while(1):
#                 x += dx[j]
#                 y += dy[j]
#
#                 if x < 0 or x >= N or y < 0 or y >= N: break    #벽
#                 if arr[x][y] == 3 : break                       #바위
#                 if arr[x][y] == 2 : ans += 1                    #토끼
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # 0:빈공간, 1:사냥군, 2:토끼, 3:바위
#     hunter =[]
#     ans = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 hunter.append((i,j))
#     solve()
#     print("#{} {}".format(tc+1, ans))