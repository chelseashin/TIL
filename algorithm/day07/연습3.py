# 초기화
# visited[], stack[] : 초기화

# DFS 알고리즘
# DFS(v)
#     v 방문;
#     visited[v] <- true;
#     do {
#     if (v의 인접 정점 중 방문 안한 w 찾기)
#         push(v);
#     while(w) {
#         w 방문;
#         visited[w] <- true;
#         push(w);
#         v <- w;
#         v의 인접 정점 중 방문 안한 w 찾기
#         }
#         v <- pop(stack);
#     }while(v)
# end DFS

# DFS 알고리즘 - 재귀
# DFS_Recursive(G, v)
#
#     visited[ v ] # <- True // v 방문 설정
#
#     for each all w in adjacency(G, v)
#         IF visited[w] != True
#     DFS_Recursive(G, w)

def dfs(v):
    global G, visited, n   # 변수가 많아지는 것을 방지하여 전역 처리
    visited[v] = 1         # 1회 방문한 것을 표현
    print(v, end = " ")

    for w in range(n):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

import sys
sys.stdin = open("연습3.txt")

n, e = map(int, input().split())
n += 1
temp = list(map(int, input().split()))

G = [[0 for i in range(n)] for j in range(n)]   # 2차원 초기화
visited = [0 for i in range(n)]  # 방문처리

for i in range(0, len(temp), 2): # 입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(n):
    print(f'{i} {G[i]}')

# dfs(G, 1, n)
dfs(1)
# 정답 예시 : 1-2-4-6-5-7-3