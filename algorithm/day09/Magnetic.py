# 나의 풀이
import sys
sys.stdin = open("Magnetic.txt")

T = 10
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)

    # 1 : N극 성질 가지는 자성체(위)
    # 2 : S극 성질 가지는 자성체(아래)

# 열을 기준으로 생각해보자. 항상 순서는 1, 2 이다.
# 0, 1로 푸는 거라면 flag라고 쓰는 것이 좋다!
    cnt = 0
    for i in range(N):   # 행
        stack = 0
        for j in range(N):  # 열
            if arr[j][i] == 1:
                stack = 1
            elif arr[j][i] == 2:
                if stack == 1:
                    cnt += 1
                    stack = 0

    print(f"#{tc + 1} {cnt}")


# 다시 풀이
import sys
sys.stdin = open("Magnetic.txt")

T = 10
for tc in range(T):
    N = int(input())
    # 데이터 불러오기 1
    # arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 데이터 불러오기 2
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    # print(arr)
    # print(len(arr))  # 100

    count = 0
    for i in range(N):
        stack = []
        for j in range(N):
            if arr[j][i] != 0:
                stack.append(arr[j][i])
    # print(stack)

    for i in range(len(stack)):
        if stack[0] == 2:
            stack.pop(0)
        elif stack[-1] == 1:
            stack.pop()

    for i in range(len(stack)-1):
        if stack[i] == 1 and stack[i+1] != 2:
            count += 1

    print(f"#{tc + 1} {count}")


# 다른 풀이
# 0을 제외한 모든 숫자를 stack에 넣어 1에서 2로 바뀔 때 count 해줌
N = 10
for test_case in range(N):
    T = int(input())
    data = [list(map(int, input().split())) for _ in range(T)]
    # print(data)

    count = 0
    for j in range(len(data)):
        stack = []
        for i in range(len(data)):
            if data[i][j] == 1 or data[i][j] == 2:
                stack.append(data[i][j])
        # print(stack)
        for i in range(len(stack)):
            if stack[0] == 2:
                stack.pop(0)
            if stack[-1] == 1:
                stack.pop()

        for i in range(len(stack) - 1):
            if stack[i] == 1 and stack[i + 1] == 2:
                count += 1

    print(f'#{test_case + 1} {count}')