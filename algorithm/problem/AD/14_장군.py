import sys
sys.stdin = open("14.txt")
#
def iswall(x, y):
    if x > -1 and y > -1 and x < 10 and y < 9:  # 벽이 아니면
        return False
    return True
#
# def bfs(xs, ys, xk, yk):


xs, ys = map(int,input().split())
xk, yk = map(int,input().split())

# 상이 갈 수 있는 곳
dx = [-2, -3, -3, -2, 2, 3, 2, 3]
dy = [-3, -2, 2, 3, -3, -2, 3, 2]

wall = [[[-1,0],[-2,-1]], [[-1,0],[-2,1]], [[0,1],[-1,2]], [[0,1],[1,2]], [[1,0],[2,1]], [[1,0],[2,-1]], [[0,-1],[1,-2]], [[0,-1],[-1,-2]]]

# 장애물 검사
wall = [[]]

visited = [[0] * 9 for i in range(10)]
print(bfs(xs, ys, xk, yk))
