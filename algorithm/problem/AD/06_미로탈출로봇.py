import sys
sys.stdin = open("06.txt")

def bfs():
    que = []
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    # 1] 시작점을 큐에 저장 (방문표시)
    que.append((sr, sc, 0)) # 행, 열, 시간을 큐에 저장
    arr[sr][sc] = 1 # 맵에 방문표시
    while que:
        # 2] 큐에서 데이터 읽기
        r, c, time = que.pop(0)
        if r == er and c == ec: return time # 도착하면 리턴
        # 3] 델타검색하면서 연결점(길)을 찾아 큐에 저장
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 3-1] 맵의 범위 체크
            if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            # 3-2] 연결점을 찾아 큐에 저장(방문표시)
            if arr[nr][nc] != 0: continue # 길이 아니면 스킵
            arr[nr][nc] = 1
            que.append((nr, nc, time + 1))
    # 4] 큐가 빈 상태(예외상황)
    return -1

C, R = map(int, input().split())
sc, sr, ec, er = map(int, input().split())
sc -= 1
sr -= 1
ec -= 1
er -= 1
arr = [list(map(int, input())) for i in range(R)]
print(bfs())