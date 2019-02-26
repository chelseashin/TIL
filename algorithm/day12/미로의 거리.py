import sys
sys.stdin = open("미로의 거리.txt")

# 시작점 찾기
def find_start(data):
    for x in range(N):
        for y in range(N):
            if data[x][y] == 2:
                return x, y
# 벽인지 판단하는 함수
def isWall(x, y):
    global N, maze
    if x < 0 or x >= N : return True  # 벽이면
    if y < 0 or y >= N : return True
    if maze[x][y] == 1: return True
    return False    # 벽이 아니면

def bfs_maze(x, y):
    global maze, visited
    queue = []  # 갈 수 있는 곳을 큐에 넣기
    visited[x][y] = 1

    queue.append((x, y))
    # maze[x][y] = 9    # 방문표시
    while queue:
        x, y= queue.pop(0)
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i in range(4):
            new_x = x + dx[i]   # i가 반복되면서 상/하/좌/우를 적용했을 때의
            new_y = y + dy[i]   # 새로운 좌표 생성
            if isWall(new_x, new_y) == False: # 벽이 아니라면
                if maze[new_x][new_y] == 3:  # 목적지를
                    return visited[x][y]-1
                if maze[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = visited[x][y] + 1
    return 0

T = int(input())
for tc in range(T):
    N = int(input())   # 5 5 5
    # 미로를 중첩 리스트로 저장
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)
    visited = [[0 for _ in range(N)]for _ in range(N)]

    # 시작할 장소의 x, y 좌표
    start_x, start_y = find_start(maze)
    result = bfs_maze(start_x, start_y)
    print(f'#{tc+1} {result}')