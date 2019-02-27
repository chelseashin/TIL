import sys
sys.stdin = open("노드의 경로.txt")

def bfs(S):  # 1에서 가장 멀리 있는 정점을 찾으시오.
    global data, G
    queue = []

    queue.append(S)  #enQueue하면서 방문처리
    visited[S] = 1
    while len(queue) != 0:
        t = queue.pop(0)
        for w in range(1, V+1):
            if data[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1
                print(w, end=" ")

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    # 2차원 초기화
    data = [[0 for i in range(V+1)] for j in range(V+1)]
    visited = [0 for i in range(V+1)]

    for i in range(E):
        x, y = map(int, input().split())
        data[x][y] = 1

    S, G = map(int, input().split())    # 출발점, 도착점
    # 데이터 확인
    # print(V, E)
    # print(data)
    # print(S, G)
    # bfs(S)
    # print("#{tc + 1} {bfs(S)}")