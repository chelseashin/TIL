# Stack 1

# 반복문자 지우기
import sys
sys.stdin = open("반복문자 지우기.txt")

T = int(input())
for tc in range(T):
    data = input()
    # print(data)

    stack = []
    for i in range(len(data)):
        if len(stack) == 0:     # 스택에 아무것도 없는 경우
            stack.append(data[i])
        else:       # 스택의 마지막 문자와 새로 들어오는 데이터 비교
            if stack[-1] != data[i]:
                stack.append(data[i])
            else:
                stack.pop()

    print(f"#{tc + 1} {len(stack)}")


# 괄호검사
import sys
sys.stdin = open("괄호검사.txt")

T = int(input())
for tc in range(T):
    data = str(input())
    # print(data)

    def make_gwalho(data):
        gwalho = ""
        g = '(){}'
        for i in range(len(data)):
            if data[i] in g:
                gwalho += data[i]
        return gwalho
    # print(make_gwalho(data))

    def check_gwalho(data):
        s = []
        for i in range(len(data)):
            if len(s) == 0:
                s.append(data[i])
            else:
                if s[-1] == '(':
                    if data[i] == ')':
                        s.pop()
                    else:
                        s.append(data[i])
                elif s[-1] == '{':
                    if data[i] == '}':
                        s.pop()
                    else:
                        s.append(data[i])
        if len(s) > 0:
            return 0
        else:
            return 1

    print(f"#{tc + 1} {check_gwalho(make_gwalho(data))}")


# 종이 붙이기
import sys
sys.stdin = open("종이붙이기.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    # print(N) # 30 50 70
    #  [1, 3, 5, 11, 21, ... ] 순으로 행렬 존재 => 점화식 찾기

    s = [1, 3]
    for i in range(2, N//10):
        # 점화식 : i =  i-2번째 값 * 2 + i-1번째 값
        i = s[-2]*2 + s[-1]
        s.append(i)

    print(f"#{tc+1} {s[-1]}")


# 그래프 경로
import sys
sys.stdin = open("그래프 경로.txt")

def dfs(v):
    global data, visited, V , G, flag  # 변수가 많아지는 것을 방지하여 전역 처리
    # 실행시간 단축하기 위해서 깊이에서 목표(G)를 만나면 재귀함수 호출 중단 장치 설정
    # flag 사용하는 경우
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

    data = [[0 for i in range(V+1)] for j in range(V+1)]   # 2차원 초기화(7X7), 0행과 0열은 사용하지 않기 때문
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
    # print(f"#{tc + 1} {flag}")
    print(f"#{tc + 1} {visited[G]}")