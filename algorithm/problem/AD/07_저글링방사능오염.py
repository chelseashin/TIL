import sys
sys.stdin = open("07.txt")

# def BFS():
#     que = []
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#
#     que.append((sr, sc, 3))
#     data[sr][sc] = 0
#     while que:
#         r, c, time = que.pop(0)
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#
#             if nr < 0 or nr >= R or nc < 0 or nc >= C:
#                 continue
#             if data[nr][nc] == 1:
#                 data[nr][nc] = 0
#                 que.append((nr, nc, time+1))
#     return time # 큐가 빈상태(더이상 없앨 저글링이 없는 경우)
#
#
# C, R = map(int, input().split())
# data = [list(map(int, input())) for _ in range(R)]
#
# sc, sr = map(int, input().split())
# sc -= 1
# sr -= 1
# print(BFS())
# print()


def isWall(x, y):
    if x < 0 or x > B-1: return True
    if y < 0 or y > A-1: return True
    return False

def Irradiate(x, y):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    Q = []
    Q.append((x, y))
    visit[x][y] = 1

    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            rex = x + dx[i]
            rey = y + dy[i]
            if not isWall(rex, rey):
                if zerg[rex][rey] == 1 and visit[rex][rey] == 0:
                    Q.append((rex, rey))
                    visit[rex][rey] = visit[x][y] + 1


A, B = map(int, input().split())
zerg = [list(map(int, input())) for _ in range(B)]
visit = [[0]*A for _ in range(B)]
tx, ty = map(int, input().split())
maxt = -1
cnt = 0

Irradiate(ty-1, tx-1)

for i in range(B):
    for j in range(A):
        if visit[i][j] > maxt:
            maxt = visit[i][j]
        if zerg[i][j] == 1 and visit[i][j] == 0:
            cnt += 1

print(maxt + 2)
print(cnt)