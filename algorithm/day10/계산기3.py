import sys
sys.stdin = open("계산기3.txt")

T = 10
for tc in range(T):
    N = int(input())
    data = input()
    # data = list(map(str, input().split()))
    print(N)
    print(data)