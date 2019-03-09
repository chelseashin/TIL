import sys
sys.stdin = open("숫자근.txt")

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
# print(num)

# 숫자근 만들어주는 함수
def root_num(data):
    while True:
        temp = list(map(int, str(data)))
        total = sum(temp)
        if total < 10:
            return total
            num = total
    # '''
    # while True:
    #  tot = 0
    #  while num:
    #     tot += num % 10
    #     num /= 10
    #     if tot<10:return total
    #         num = tot
    # '''

rmax = 0   # 숫자근 최댓값
sol = 0
for i in range(n):
    root = root_num(num[i])  # 숫자근 만들어주는 함수
    # 가장 큰 숫자근이면 해당 정수를 솔루션으로
    if rmax < root:
        rmax = root
        sol = num[i]
    # 가장 큰 숫자근과 같다면 더 작은 솔루션으로
    if rmax == root:
        if sol > num[i]:
            sol = num[i]

print(sol)