import sys
sys.stdin = open("Contact.txt")

def bfs(S):
    global visited, arr
    queue = []
    queue.append(S)
    while len(queue) != 0:
        S = queue.pop(0)
        for i in arr[S]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[S] + 1

T = 10
for tc in range(T):
    N, S = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    data = list(map(int, input().split()))