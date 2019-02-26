import sys
sys.stdin = open("회전.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    num = M % N
    print(f"#{tc + 1} {data[num]}")
