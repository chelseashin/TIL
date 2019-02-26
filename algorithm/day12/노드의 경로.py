import sys
sys.stdin = open("노드의 경로.txt")

def bfs(S):
    global data, G
    queue = []
    queue.append(S)

    visited[S] = 1
    while len(queue) != 0:
        t = queue.pop(0)
        for w in range(1, V+1):
            if data[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t]+1
    if visited[G] == 0:
        return 0
    else:
        return visited[G] - 1

T = int(input())
for tc in range(T):
    flag = 0
    V, E = map(int, input().split())

    data = [[0 for i in range(V + 1)] for j in range(V + 1)]  # 2차원 초기화
    visited = [0 for i in range(V + 1)]  # 방문처리

    for i in range(E):  # 입력
        x, y = map(int, input().split())
        # 인접행렬 만들기
        data[x][y] = 1
        data[y][x] = 1
    S, G = map(int, input().split())
    # print(data)

    print(f"#{tc + 1} {bfs(S)}")