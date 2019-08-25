import sys
sys.stdin = open('21_input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(sr, sc):


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
L = []
count = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            dfs(i, j)


print(count)
for i in dr:
    print(i)