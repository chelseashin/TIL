import sys
sys.stdin = open("그래프 경로.txt")

def dfs(v):
    global data, visited, V , G, flag  # 변수가 많아지는 것을 방지하여 전역 처리
    # 실행시간 단축하기 위해서 깊이에서 목표(G)를 만나면 재귀함수 호출 중단 장치 설정
    # if v == G:
    #     flag = 1
    #     return
    visited[v] = 1         # 1회 방문한 것을 표현

    for w in range(V+1):
        if data[v][w] == 1 and visited[w] == 0:
            dfs(w)    # 재귀호출

T = int(input())
for tc in range(T):
    flag = 0
    V, E = map(int, input().split())

    data = [[0 for i in range(V+1)] for j in range(V+1)]   # 2차원 초기화
    visited = [0 for i in range(V+1)]  # 방문처리

    for i in range(E):  # 입력
        x, y = map(int, input().split())
        data[x][y] = 1
        
    S, G = map(int, input().split())
    # 데이터 확인
    # print(V, E)
    # print(data)
    # # print(len(data))    # 10 8 18
    # print(S, G)
    dfs(S)

    # print(visited[G])
    # print(flag)
    # print(f"#{tc+1} {flag}")
    print(f"#{tc + 1} {visited[G]}")