import sys
sys.stdin = open("ex.txt", "r")

T = int(input())
N, M = map(int, input().split())     # 10, 5

field = []
for i in range(N):
    row = input()
    field.append(row)
print(field)

# 한 줄로 받기
# L = [list(map(int, input())) for _ in range(N)]
# print(L)