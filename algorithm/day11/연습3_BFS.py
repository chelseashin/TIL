import sys
sys.stdin = open("연습3.txt")


def bfs(v):  # 탐색 시작점 : v
    global V, E
    visited = [0] * (V+1)    # 방문처리 : 정점의 개수 V
    queue = []    # 큐 생성
    queue.append(v)    # 시작점 v를 큐에 삽입
    while queue:    # 큐가 비어있지 않은 경우 = while len(queue) != 0:
        v = queue.pop(0)    # 큐의 첫번째 원소 반환
        if not visited[v]:  # 방문되지 않은 곳이라면
            visited[v] = 1  # 방문한 것으로 표시
            print(v, end = "-")  # 보기
            for i in range(V+1):    # v에 인접한 모든 정점을 구하려면
                if G[v][i] == 1 and visited[i] == 0:
                    queue.append(i)    # 큐에 넣기

        # for i in G[t]:    # t와 연결된 모든 선에 대해
        #     if not visited[i]:    # 방문되지 않은 곳이라면
        #         queue.append(i)


V, E = map(int, input().split())  # 정점의 개수: V, 간선의 개수 : E
data = list(map(int, input().split()))
# print(V, E)
# print(data)

# n+1해줘야 함! 0행, 0열이 있기 때문.
G = [[0 for i in range(V+1)] for j in range(V+1)]    # 2차원 초기화

for i in range(0, len(data), 2):
    G[data[i]][data[i+1]] = 1
    G[data[i+1]][data[i]] = 1

for i in range(V):
    print(f'{i} {G[i]}')

bfs(1)
# -1-2-3-4-5-7-6