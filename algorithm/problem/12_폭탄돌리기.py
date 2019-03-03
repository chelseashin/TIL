import sys
sys.stdin = open("폭탄돌리기.txt")

K = int(input())
N = int(input())
# 방법 1
# for i in range(N):
#     quiz = list(map(str, input().split()))
#     print(quiz)

# 방법 2
# quiz = [input().split() for _ in range(N)]

# 방법 3
quiz = [list(map(str, input().split())) for _ in range(N)]
time = 210

while quiz and time:
    number = quiz.pop(0)
    time -= int(number[0])
    if time < 0:
        break
    if number[1] == 'T':
        if K < 8:
            K += 1
        else:
            -7
print(K)