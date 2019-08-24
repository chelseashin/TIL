import sys
sys.stdin = open('19_input.txt')

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(sr, sc):
    global arr, visited, N, M
    Q = [(sr, sc)]
    visited[sr, sc] = 1
    while Q:
        r, c = Q.pop(0)
        if r == N-1 and c == M-1:
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if arr[nr][nc]



N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * (M) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            arr[i][j] = 0
            bfs(0, 0)

print(visited[N-1][M-1])