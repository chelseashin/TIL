import sys
sys.stdin = open("10_input.txt")

def dfs(v):
    global N, A, visited
    # visited[v] = 1
    stack = [v]
    while stack:
        start = stack.pop()
        if visited[start] == 1:
            continue
        visited[start] = 1
        print(start, end=' ')
        for i in range(N, 0, -1):
            if A[start][i] == 1 and visited[i] == 0:
                stack.append(i)


N, M, V = map(int, input().split())
A = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for m in range(M):
    start, end = map(int, input().split())
    A[start][end] = 1
    A[end][start] = 1
dfs(V)

