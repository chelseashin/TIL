import sys
sys.stdin = open("줄세우기.txt")

N = int(input())    # 학생 수 : 5
numbers = list(map(int, input().split()))  # 뽑은 카드 번호 : [0, 1, 1, 3, 2]

line = []
for i in range(N):
    num = numbers.pop(0)
    if num:
        line = line[:-num] + [i+1] + line[-num:]
    else:
        line += [i+1]

for i in range(len(line)):
    print(line[i], end = " ")

# print(*line)